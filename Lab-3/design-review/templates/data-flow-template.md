# Data Flow Template

Trace one specific user action through every layer of your system. Choose your most important AI feature.

**Feature being traced:**

---

## Step 1 — User Action

What exactly does the user do? Be specific about the UI element and the action.

```
The user [clicks / types / uploads / speaks] [what] on [which screen / component].

Example: "The user clicks 'Analyse Receipt' after uploading a photo on the Upload screen."
```

---

## Step 2 — Preprocessing

What happens to the input before any API call is made?

```
The [input type] is [what happens to it].

Examples:
- "The uploaded image is resized to a maximum dimension of 1280px and compressed to JPEG."
- "The user's text is trimmed of whitespace and checked for minimum length (10 characters)."
- "The uploaded PDF is parsed to plain text using [library]."
- "No preprocessing — the input is passed directly."
```

---

## Step 3 — Prompt Construction

How is the prompt built? What goes into the system prompt and what goes into the user message?

```
System prompt: [describe what it contains — instructions, persona, output format specification]

User message content: [what is inserted — user text, image as base64, document text, retrieved context]

Example:
System prompt: "You are a receipt extraction assistant. Extract the following fields as JSON:
amount (number), date (YYYY-MM-DD), vendor (string). Return only valid JSON."

User message: [the uploaded image as base64, with the instruction "Extract fields from this receipt."]
```

---

## Step 4 — API Call

Which model, via which route, with which parameters?

```
Model: [e.g., gemini-3-flash-preview]
Route: [e.g., OpenRouter at openrouter.ai/api/v1, or direct Google AI API]
Key parameters: [max_tokens, temperature, response_format if applicable]

Example:
Model: openai/dall-e-3 via OpenRouter
Parameters: size="1024x1024", quality="standard", n=1
```

---

## Step 5 — Response Parsing

What does the API return and how do you extract what you need?

```
The API returns: [text / JSON string / image URL / audio binary / structured object]
We extract: [describe specifically what fields or content you pull out]
We handle malformed responses by: [what happens if parsing fails]

Example:
"The API returns a JSON string inside response.choices[0].message.content.
We parse it with json.loads(). If parsing fails (JSONDecodeError), we
set all fields to None and trigger the low-confidence fallback path."
```

---

## Step 6 — Confidence or Validation

How do you decide whether to show the result?

```
We check: [what signal — explicit confidence score, field completeness, model's own hedging language, none]
Threshold: [the value above which we show directly, below which we flag or hide]
If below threshold: [what happens next — fallback path, human review, manual entry prompt]

Example:
"If all three fields (amount, date, vendor) parsed successfully: show directly.
If any field is null: show with amber highlight and 'Please verify' label.
If JSON parsing failed entirely: trigger the full fallback UX."
```

---

## Step 7 — User Output

What appears on screen? Include both the success path and the fallback path.

```
Success path: The user sees [describe exactly what is displayed].

Fallback path: The user sees [describe what appears when step 6 fails].

Example success: "The three extracted fields appear pre-filled in the expense form.
Each field has a green tick. The user can edit any field before confirming."

Example fallback: "Fields with null values appear as empty input boxes highlighted
in amber. The label 'Could not read — please enter manually' appears above them.
No error code or technical message is shown."
```
