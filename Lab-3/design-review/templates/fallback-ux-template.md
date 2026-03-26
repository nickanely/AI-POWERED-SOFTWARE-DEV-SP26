# Fallback UX Template

Describe what the user sees when your AI fails, is unavailable, or returns a low-confidence answer. Write from the user's perspective, not the developer's.

---

## Identify Your Fallback Scenarios

Check the scenarios that apply to your product:

- [ ] **API failure** — the model call times out, returns a 500 error, or the network is unavailable
- [ ] **Low-confidence output** — the model returns a result but it is uncertain or incomplete
- [ ] **Content filter rejection** — a user prompt is rejected by the model's safety system
- [ ] **Rate limit hit** — the API rejects the call because of too many requests

---

## Write the Fallback for Each Scenario That Applies

### API failure

```
The user sees:
[describe the visual — a banner, inline message, replaced spinner, modal]

The message reads:
"[write the actual words — not placeholders, the real text]"

The action available to the user:
[retry button / contact support / save and come back / nothing needed]

What is NOT shown:
[stack traces, error codes, HTTP status, the word "AI", raw exception messages]
```

### Low-confidence output

```
The user sees:
[describe what changes visually to communicate uncertainty]

The message reads:
"[write the actual words]"

The threshold for this state:
[above X% = shown normally | between X% and Y% = shown with warning | below Y% = hidden with manual entry]

The action available to the user:
[edit the field manually / request re-analysis / accept anyway / flag for review]
```

### Content filter rejection (if applicable)

```
The user sees:
"[write the actual words — not 'error', not 'policy violation', something human]"

The action available to the user:
[rephrase the prompt / contact support / try a different approach]
```

---

## One-Paragraph Summary

After filling in the scenarios above, write a one-paragraph summary for Section 7 of DESIGN-REVIEW.md. Start with "The user sees..." and cover your most important fallback scenario.

```
[write here]
```
