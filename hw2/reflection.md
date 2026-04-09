# HW2 Data Governance Reflection

**Course:** CS-AI-2025 — Building AI-Powered Applications | Spring 2026
**Student:** Nikoloz Aneli
**Assignment:** Homework 2 — Individual Audio Pipeline

---

## Question 1 — Consent

If this pipeline processed real user audio instead of synthetic TTS output, the consent requirements would be significantly more demanding than what my current script handles.

A real consent screen would need to appear before the microphone activates or before any audio file is uploaded. It would need to say something like: "Before you continue, please note that the audio you record or upload will be sent to OpenAI's Whisper API for transcription. Audio is transmitted over an encrypted connection and is not retained by this application after processing. OpenAI's API data policy states that API inputs are not used for model training as of the time of writing. By clicking 'Continue', you confirm you have the right to process this audio and consent to it being sent for transcription."

Three things stand out as non-negotiable. First, the consent notice must appear before recording begins, not after. This is required under GDPR Article 13 and is basic ethical practice — you cannot retroactively consent someone to data processing that already happened. Second, the user must be able to revoke consent after the fact. In my pipeline, this is simple because the raw MP3 file is saved locally — a "Delete my audio" button would simply call `os.remove()` on the file and send a deletion request to whatever backend stores the transcript. Third, if the audio contains a third party's voice (e.g., a recorded meeting), the person speaking also has rights. My pipeline makes no attempt to detect or handle this. A production system would need to warn the user explicitly: "Only upload audio you have the right to process."

---

## Question 2 — Retention

Retention policy should match the sensitivity of the use case and the minimum necessary period.

For a study app that generates TTS audio lessons (similar to what my pipeline produces), the audio files are synthetic and contain no personal voice data. Retaining them as cached assets for 30–90 days is reasonable to avoid re-generating the same content. The transcript, if stored, is essentially the original text, which is not sensitive. A 90-day retention on cached audio with automatic expiration is appropriate.

For a customer service transcription tool, the calculus changes immediately. Transcripts likely contain names, account numbers, complaints, and emotional context. The audio may contain background voices the customer did not intend to capture. In this case, the raw audio should be deleted immediately after transcription — within seconds of the API returning a result. The transcript itself is a business record and would likely be retained for the duration of the customer relationship plus a defined archival period (often 3–7 years under financial regulations).

For a medical intake form, audio is likely to contain health information and is therefore subject to HIPAA in the US and equivalent regulations in Georgia. Raw audio must be deleted immediately after transcription. The transcript is protected health information and must be stored encrypted, with access logging, and for a period defined by the applicable regulation (typically 6 years under HIPAA). In this context, even my simple JSONL cost log — which records file names and audio durations — should be treated as potentially sensitive metadata.

---

## Question 3 — PII in Audio vs. Text

Audio carries PII risks that text does not, and my pipeline run made this concrete in at least two ways.

The most obvious difference is voice biometrics. The MP3 files my pipeline generates via TTS do not contain a real human voice, so this risk does not apply. But if a user uploaded a recording of themselves, their voiceprint is embedded in the file. A voiceprint can uniquely identify an individual even when all spoken words have been removed or redacted. Text extracted from that same audio would contain none of this biometric data. The raw audio file is the more dangerous artifact, which is why I do not store it anywhere beyond the local `audio-output/` directory, and why the governance checklist recommends deleting audio files after processing.

The second risk is metadata embedded in audio files. The WAV and M4A formats in particular can embed creation timestamp, device model, and in some cases GPS coordinates. None of this appears in the transcript. My pipeline reads the file extension but does not strip metadata before sending the file to the API — a gap I would address in a production version by running the file through `ffmpeg -map_metadata -1` before the API call.

The third risk is ambient content. If a user recorded their voice in a shared space, the recording may contain background conversations from people who did not consent to any processing. A transcript might capture some of this, but the raw audio captures all of it, including voices, context, and emotional tone that NLP alone would not surface. My pipeline has no way to detect or handle this.

---

## Question 4 — SmartCV Capstone

My team's Exercise 3 audio decision for SmartCV was to defer audio — it adds value but is not required for the MVP. The core product (CV analysis and job match) is entirely text-based, and the response time constraints of voice interaction would actually slow down a workflow that currently runs under 90 seconds.

However, if we did add audio to SmartCV later, the governance implications would be meaningful. The most natural audio feature would be a "read my interview questions aloud" button using TTS — this is low-risk because it generates synthetic audio from AI-produced text and involves no user voice data at all. Retention is trivial: generate on demand, stream to the browser, never store.

A more ambitious feature — "record yourself answering and get AI feedback" — would be in a different risk category. That would capture a user's voice, potentially in a quiet room with identifiable background sounds, and send it to Whisper via OpenRouter. For this feature, we would need: an explicit consent banner before the microphone activates, automatic deletion of the audio file within 10 seconds of transcription completing, a clear disclosure that voice data is processed by a third-party API, and a "skip audio" option so the feature is never required. The transcript itself, like all SmartCV output, would be tied to an anonymous session ID and auto-deleted after 7 days — consistent with the data governance plan already in our Design Review.

---

*Word count: approximately 870 words.*
*Reflection written in reference to the HW2 pipeline run on 9 April 2026.*
