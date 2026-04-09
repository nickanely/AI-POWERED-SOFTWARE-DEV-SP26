"""
HW2: Individual Audio Pipeline
CS-AI-2025 -- Building AI-Powered Applications | Spring 2026
Kutaisi International University

Round-trip pipeline: Text --> TTS (MP3) --> STT (transcript) --> Comparison
Cost and latency tracked for every API call.

SETUP:
  pip install openai python-dotenv
  Create .env with:
    OPENROUTER_API_KEY=sk-or-v1-your-key-here
    OPENAI_API_KEY=sk-your-openai-key-here  (audio goes direct to OpenAI)

RUN:
  python hw2-audio-pipeline.py
  python hw2-audio-pipeline.py "Your custom text here"
  python hw2-audio-pipeline.py --transcribe path/to/audio.mp3
"""

import os
import sys
import time
import json
import argparse
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI, APIConnectionError, APITimeoutError, APIStatusError

# ── Setup ──────────────────────────────────────────────────────────────────

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

missing_keys = [k for k, v in {"OPENROUTER_API_KEY": api_key, "OPENAI_API_KEY": openai_key}.items() if not v]
if missing_keys:
    for k in missing_keys:
        print(f"ERROR: {k} not found in .env")
    sys.exit(1)

# openrouter for text/llm calls
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

# openai directly for audio — openrouter doesn't support /audio/* endpoints
audio_client = OpenAI(api_key=openai_key)

OUTPUT_DIR = Path("audio-output")
OUTPUT_DIR.mkdir(exist_ok=True)

COST_LOG_FILE = Path("audio-cost-log.jsonl")

SUPPORTED_FORMATS = {".mp3", ".mp4", ".wav", ".webm", ".m4a", ".mpeg", ".mpga"}

DEFAULT_TEXT = (
    "Machine learning models learn patterns from data. "
    "They generalize from training examples to make predictions "
    "on new, unseen inputs. The quality of the training data "
    "directly determines the quality of the model's predictions. "
    "Building AI-powered applications requires understanding both "
    "the capabilities and the limitations of these systems."
)

VOICES = ["nova", "alloy"]  # Two voices demonstrated as required


# ── Cost and Latency Tracking ──────────────────────────────────────────────

call_log: list[dict] = []


def record_call(call_type: str, model: str, latency: float,
                input_size: str, cost: float, metadata: dict = None):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "call_type": call_type,
        "model": model,
        "latency_seconds": round(latency, 2),
        "input_size": input_size,
        "cost_usd": round(cost, 6),
        "metadata": metadata or {},
    }
    call_log.append(entry)
    with open(COST_LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


def tts_cost(char_count: int, model: str = "tts-1") -> float:
    rate = 0.015 if model == "tts-1" else 0.030
    return (char_count / 1000) * rate


def stt_cost(duration_seconds: float) -> float:
    return (duration_seconds / 60) * 0.006


# ── Text to Speech ─────────────────────────────────────────────────────────

def text_to_speech(text: str, voice: str, filename: str,
                   retries: int = 1) -> dict:
    """
    Generate speech from text using OpenAI TTS directly.
    Returns a result dict with success flag, path, timing, and cost.
    """
    output_path = OUTPUT_DIR / filename
    attempt = 0

    while attempt <= retries:
        attempt += 1
        start = time.time()
        try:
            response = audio_client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text,
                response_format="mp3",
            )
            response.stream_to_file(str(output_path))
            elapsed = round(time.time() - start, 2)
            file_size_kb = output_path.stat().st_size / 1024
            cost = tts_cost(len(text))

            record_call(
                call_type="tts",
                model="tts-1",
                latency=elapsed,
                input_size=f"{len(text)} chars",
                cost=cost,
                metadata={"voice": voice, "file": str(output_path)},
            )

            return {
                "success": True,
                "path": str(output_path),
                "voice": voice,
                "latency": elapsed,
                "file_size_kb": round(file_size_kb, 1),
                "cost": cost,
                "char_count": len(text),
            }

        except APITimeoutError:
            elapsed = round(time.time() - start, 2)
            if attempt <= retries:
                print(f"    [Retry {attempt}] TTS timed out after {elapsed}s. Retrying...")
                time.sleep(1)
            else:
                record_call("tts", "tts-1", elapsed, f"{len(text)} chars", 0.0,
                            {"error": "timeout", "voice": voice})
                return {"success": False, "error": "API timed out after retry.",
                        "voice": voice, "latency": elapsed}

        except APIConnectionError as e:
            elapsed = round(time.time() - start, 2)
            if attempt <= retries:
                print(f"    [Retry {attempt}] Connection error. Retrying...")
                time.sleep(2)
            else:
                record_call("tts", "tts-1", elapsed, f"{len(text)} chars", 0.0,
                            {"error": str(e), "voice": voice})
                return {"success": False, "error": f"Connection failed: {e}",
                        "voice": voice, "latency": elapsed}

        except APIStatusError as e:
            elapsed = round(time.time() - start, 2)
            record_call("tts", "tts-1", elapsed, f"{len(text)} chars", 0.0,
                        {"error": str(e), "voice": voice})
            return {"success": False, "error": f"API error {e.status_code}: {e.message}",
                    "voice": voice, "latency": elapsed}


# ── Speech to Text ─────────────────────────────────────────────────────────

def speech_to_text(audio_path: str, retries: int = 1) -> dict:
    """
    Transcribe an audio file using OpenAI Whisper directly.
    Validates format and file size before sending.
    """
    path = Path(audio_path)

    # Validation — handle errors gracefully, no raw stack traces
    if not path.exists():
        return {"success": False,
                "error": f"File not found: {audio_path}\nCheck the path and try again."}

    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_FORMATS:
        return {"success": False,
                "error": (f"Unsupported format '{suffix}'.\n"
                          f"Accepted formats: {', '.join(sorted(SUPPORTED_FORMATS))}")}

    file_size_mb = path.stat().st_size / (1024 * 1024)
    if file_size_mb > 25:
        return {"success": False,
                "error": (f"File too large ({file_size_mb:.1f} MB). "
                          "Maximum is 25 MB. Trim to under 30 seconds.")}

    attempt = 0
    while attempt <= retries:
        attempt += 1
        start = time.time()
        try:
            with open(path, "rb") as f:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=f,
                    response_format="verbose_json",
                )
            elapsed = round(time.time() - start, 2)
            duration = getattr(transcript, "duration", 0) or 0
            cost = stt_cost(duration)

            record_call(
                call_type="stt",
                model="whisper-1",
                latency=elapsed,
                input_size=f"{file_size_mb:.2f} MB",
                cost=cost,
                metadata={"audio_duration_s": duration,
                          "language": getattr(transcript, "language", "unknown")},
            )

            return {
                "success": True,
                "text": transcript.text,
                "language": getattr(transcript, "language", "unknown"),
                "duration_seconds": duration,
                "latency": elapsed,
                "cost": cost,
                "file": path.name,
            }

        except APITimeoutError:
            elapsed = round(time.time() - start, 2)
            if attempt <= retries:
                print(f"    [Retry {attempt}] STT timed out. Retrying...")
                time.sleep(1)
            else:
                record_call("stt", "whisper-1", elapsed, f"{file_size_mb:.2f} MB", 0.0,
                            {"error": "timeout"})
                return {"success": False, "error": "STT timed out after retry.",
                        "latency": elapsed}

        except APIConnectionError as e:
            elapsed = round(time.time() - start, 2)
            if attempt <= retries:
                print(f"    [Retry {attempt}] Connection error. Retrying...")
                time.sleep(2)
            else:
                record_call("stt", "whisper-1", elapsed, f"{file_size_mb:.2f} MB", 0.0,
                            {"error": str(e)})
                return {"success": False, "error": f"Connection failed: {e}",
                        "latency": elapsed}

        except APIStatusError as e:
            elapsed = round(time.time() - start, 2)
            record_call("stt", "whisper-1", elapsed, f"{file_size_mb:.2f} MB", 0.0,
                        {"error": str(e)})
            return {"success": False,
                    "error": f"API error {e.status_code}: {e.message}",
                    "latency": elapsed}


# ── Text Comparison ────────────────────────────────────────────────────────

def compare_texts(original: str, transcribed: str) -> dict:
    """Word-overlap accuracy between original and transcribed text."""
    orig_words = original.lower().split()
    trans_words = transcribed.lower().split()
    orig_set = set(orig_words)
    trans_set = set(trans_words)
    overlap = orig_set & trans_set
    accuracy = (len(overlap) / len(orig_set) * 100) if orig_set else 0.0
    missing = sorted(orig_set - trans_set)[:8]
    extra = sorted(trans_set - orig_set)[:8]
    return {
        "accuracy_pct": round(accuracy, 1),
        "original_words": len(orig_words),
        "transcribed_words": len(trans_words),
        "missing": missing,
        "extra": extra,
    }


# ── Cost and Latency Summary ───────────────────────────────────────────────

def print_summary():
    tts_calls = [c for c in call_log if c["call_type"] == "tts"]
    stt_calls = [c for c in call_log if c["call_type"] == "stt"]

    tts_cost_total = sum(c["cost_usd"] for c in tts_calls)
    stt_cost_total = sum(c["cost_usd"] for c in stt_calls)
    tts_avg_lat = (sum(c["latency_seconds"] for c in tts_calls) / len(tts_calls)
                   if tts_calls else 0)
    stt_avg_lat = (sum(c["latency_seconds"] for c in stt_calls) / len(stt_calls)
                   if stt_calls else 0)

    print("\n" + "=" * 60)
    print("COST AND LATENCY SUMMARY")
    print("=" * 60)
    print(f"  TTS calls:    {len(tts_calls):2d}  |  "
          f"Total cost: ${tts_cost_total:.5f}  |  "
          f"Avg latency: {tts_avg_lat:.2f}s")
    print(f"  STT calls:    {len(stt_calls):2d}  |  "
          f"Total cost: ${stt_cost_total:.5f}  |  "
          f"Avg latency: {stt_avg_lat:.2f}s")
    print(f"  Pipeline total cost: ${tts_cost_total + stt_cost_total:.5f}")
    print(f"  Full call log: {COST_LOG_FILE}")

    # Scale projection
    cost_per_run = tts_cost_total + stt_cost_total
    if cost_per_run > 0:
        print(f"\n  At scale (same pipeline, default text):")
        for users, calls in [(10, 5), (100, 5), (1000, 5)]:
            daily = cost_per_run * users * calls
            print(f"    {users:5d} users × {calls} calls/day → "
                  f"~${daily:.2f}/day  (~${daily * 30:.2f}/month)")


# ── Main Pipeline ──────────────────────────────────────────────────────────

def run_pipeline(text: str):
    print("\n" + "=" * 60)
    print("HW2 AUDIO PIPELINE")
    print("=" * 60)

    tts_results = []
    primary_audio = None

    # ── Step 1 & 2: TTS for each voice ────────────────────────────────
    for i, voice in enumerate(VOICES, 1):
        print(f"\n[{i}/{len(VOICES) + 2}] Generating speech — voice: {voice}")
        print(f"  Text ({len(text)} chars): \"{text[:60]}...\"")
        filename = f"voice_{voice}_sample.mp3"
        result = text_to_speech(text, voice, filename)

        if result["success"]:
            print(f"  Generated in {result['latency']}s")
            print(f"  File: audio-output/{filename} ({result['file_size_kb']} KB)")
            print(f"  Cost: ${result['cost']:.5f}")
            tts_results.append(result)
            if primary_audio is None:
                primary_audio = result["path"]  # Use first voice for STT
        else:
            print(f"  ERROR: {result['error']}")

    if primary_audio is None:
        print("\nPipeline halted: no audio was generated successfully.")
        print_summary()
        return

    # ── Step 3: STT ────────────────────────────────────────────────────
    step = len(VOICES) + 1
    print(f"\n[{step}/{len(VOICES) + 2}] Transcribing: {primary_audio}")
    stt_result = speech_to_text(primary_audio)

    if not stt_result["success"]:
        print(f"  ERROR: {stt_result['error']}")
        print_summary()
        return

    print(f"  Transcript: \"{stt_result['text'][:80]}...\"")
    print(f"  Language detected: {stt_result['language']}")
    print(f"  Audio duration: {stt_result['duration_seconds']:.1f}s")
    print(f"  Transcribed in {stt_result['latency']}s")
    print(f"  Cost: ${stt_result['cost']:.5f}")

    # ── Step 4: Comparison ─────────────────────────────────────────────
    step += 1
    print(f"\n[{step}/{len(VOICES) + 2}] Comparing original vs transcribed text")
    cmp = compare_texts(text, stt_result["text"])

    # Side-by-side print (truncated to 80 chars per line for readability)
    orig_words = text.split()
    trans_words = stt_result["text"].split()
    print(f"\n  {'ORIGINAL':<42}  {'TRANSCRIBED'}")
    print(f"  {'-'*42}  {'-'*42}")
    for o, t in zip(orig_words[:12], trans_words[:12]):
        match = "  " if o.lower().rstrip(".,") == t.lower().rstrip(".,") else "!!"
        print(f"  {o:<42}  {t}  {match}")
    if len(orig_words) > 12:
        print(f"  ... ({len(orig_words) - 12} more words)")

    print(f"\n  Word overlap accuracy: {cmp['accuracy_pct']}%")
    print(f"  Original words:    {cmp['original_words']}")
    print(f"  Transcribed words: {cmp['transcribed_words']}")
    if cmp["missing"]:
        print(f"  Words in original but not transcript: {', '.join(cmp['missing'])}")
    if cmp["extra"]:
        print(f"  Words in transcript but not original:  {', '.join(cmp['extra'])}")

    print_summary()
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)


def run_transcribe_only(audio_path: str):
    """Standalone transcription mode: python hw2-audio-pipeline.py --transcribe file.mp3"""
    print(f"\nTranscribing: {audio_path}")
    result = speech_to_text(audio_path)
    if result["success"]:
        print(f"\nTranscript:\n{result['text']}")
        print(f"\nLanguage: {result['language']}")
        print(f"Duration: {result['duration_seconds']:.1f}s")
        print(f"Time:     {result['latency']}s")
        print(f"Cost:     ${result['cost']:.5f}")
    else:
        print(f"\nTranscription failed: {result['error']}")
    print_summary()


# ── Entry Point ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="HW2 Audio Pipeline — TTS + STT round-trip"
    )
    parser.add_argument(
        "text", nargs="?", default=None,
        help="Text to synthesize (optional; uses default if omitted)"
    )
    parser.add_argument(
        "--transcribe", metavar="AUDIO_FILE",
        help="Skip TTS and transcribe an existing audio file"
    )
    args = parser.parse_args()

    if args.transcribe:
        run_transcribe_only(args.transcribe)
    else:
        text = args.text if args.text else DEFAULT_TEXT
        run_pipeline(text)


if __name__ == "__main__":
    main()
