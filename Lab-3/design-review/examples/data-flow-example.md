# Example: Prompt and Data Flow

The complete trace below is for the same fictional EdTech tutoring app (StudyLens). It shows what a 3.0-scoring data flow looks like. Adapt the structure — not the content — for your own product.

---

## Feature being traced: "Explain this homework problem"

**Step 1 — User action**

The user uploads a photo of their handwritten maths homework using the drag-and-drop area on the Upload screen, types their question ("I don't understand step 3") into the text field, and clicks the blue "Get explanation" button.

**Step 2 — Preprocessing**

The uploaded image file is checked for size (rejected if over 10 MB with a user-facing message). If it passes, it is resized to a maximum dimension of 1280px on the longer side, preserving aspect ratio. It is compressed to JPEG at 85% quality to reduce API payload size. The resulting bytes are base64-encoded. The user's question text is trimmed of leading/trailing whitespace and truncated to 500 characters if longer.

**Step 3 — Prompt construction**

System prompt (fixed per request, not user-editable):
> "You are a patient maths tutor for secondary school students. When given an image of handwritten homework and a student's question, identify the specific step the student is asking about and explain it in plain language. Break your explanation into numbered steps. Use simple vocabulary. Do not simply give the answer — guide the student to understand the method. Respond only in the language of the student's question."

User message content array:
- Item 1: `{ "type": "image_url", "image_url": { "url": "data:image/jpeg;base64,[encoded bytes]" } }`
- Item 2: `{ "type": "text", "text": "Student question: I don't understand step 3" }`

**Step 4 — API call**

Model: `google/gemini-3-flash` via OpenRouter (`https://openrouter.ai/api/v1`)
Parameters: `max_tokens=1024`, `temperature=0.3` (low temperature for consistency in educational explanations)
Timeout: 10 seconds. On timeout: trigger API failure fallback.

**Step 5 — Response parsing**

The API returns a plain text string in `response.choices[0].message.content`. No JSON parsing needed — the response is the explanation directly. We check that the response is non-empty and longer than 50 characters (shorter responses indicate a refusal or error). If the response starts with "I cannot" or "I'm unable", we treat it as a soft failure and route to the low-confidence path.

**Step 6 — Confidence or validation**

We do not have an explicit confidence score from this API call. We use a heuristic:
- Response is non-empty, longer than 50 chars, and does not start with a refusal phrase → display directly.
- Response is empty or shorter than 50 chars → trigger API failure fallback.
- Response starts with a refusal phrase → show the low-confidence fallback with a rephrase suggestion.

**Step 7 — User output**

Success path: The explanation appears in a styled card below the upload area. It is rendered as numbered steps (we detect numbered lists in the response and apply CSS list styling). The student's original photo is shown as a thumbnail alongside. A "Was this helpful?" two-button feedback widget appears at the bottom.

Fallback path (API failure): The spinner is replaced with: "We could not process your question right now. Your photo is still here — try again in a moment." A "Try again" button re-submits the same request. The photo is not lost.

Fallback path (soft refusal): "Our tutor could not find that step in the photo. Try re-uploading with better lighting, or rephrase your question to describe the specific calculation." A rephrasing prompt appears.
