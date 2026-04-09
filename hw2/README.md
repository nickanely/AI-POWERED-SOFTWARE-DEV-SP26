# HW2: Individual Audio Pipeline

Round-trip TTS → STT pipeline using OpenAI TTS (`tts-1`) and Whisper (`whisper-1`) via OpenRouter, with cost tracking and error handling.

---

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create your .env file
cp .env.example .env
# Then open .env and paste your OpenRouter key
```

---

## Usage

**Run the full pipeline** (TTS with two voices → transcription → comparison):
```bash
python hw2-audio-pipeline.py
```

**Run with custom text:**
```bash
python hw2-audio-pipeline.py --text "Your text here"
```

**Transcribe an existing audio file only:**
```bash
python hw2-audio-pipeline.py --transcribe path/to/audio.mp3
```

---

## Expected Output

```
============================================================
  HW2 Audio Pipeline
============================================================

--- PART 1: Text to Speech ---

[TTS] Voice: nova
      Text : "A well-written CV opens doors that a generic one never will..."
      Done : 2.14s | 47.3 KB | ~$0.0021

[TTS] Voice: alloy
      Text : "A well-written CV opens doors that a generic one never will..."
      Done : 1.98s | 45.8 KB | ~$0.0021

--- PART 2: Speech to Text ---

[STT] File : voice_nova_sample.mp3 (0.05 MB)
      Done : 1.52s | audio 8.3s | ~$0.0008
      Text : "A well-written CV opens doors that a generic one never will..."

--- PART 3: Round-Trip Comparison ---

  Original   : "A well-written CV opens doors..."
  Transcribed: "A well-written CV opens doors..."

  Word overlap accuracy : 100.0%
  Original words        : 60
  Transcribed words     : 61

--- COST AND LATENCY SUMMARY ---

  TTS calls  : 2 | Total cost: $0.0042 | Avg latency: 2.06s
  STT calls  : 1 | Total cost: $0.0008 | Avg latency: 1.52s
  Pipeline total cost : $0.0050
  Full log saved to   : audio-cost-log.jsonl

============================================================
  Pipeline complete
============================================================
```

---

## Files

| File | Description |
|---|---|
| `hw2-audio-pipeline.py` | Main pipeline script |
| `reflection.md` | Data governance reflection (870 words) |
| `requirements.txt` | Python dependencies |
| `.env.example` | API key template |
| `audio-output/` | Generated MP3 files (two voices) |
| `audio-cost-log.jsonl` | Per-call cost and latency log (generated at runtime) |
