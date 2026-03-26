# Guide: Fallback UX

The fallback UX section is the most commonly wrong section in every Design Review. Teams describe error handling code. The Design Review asks for a user experience.

---

## The Distinction

**Error handling (not what we want):**
"We will use try/except to catch API exceptions. If the API call fails, we return an HTTP 500 error. If confidence is low, we log the event and return an empty response."

This describes what happens inside your backend. The user sees nothing — or worse, a raw error.

**Fallback UX (what we want):**
"If the API call fails or takes more than 5 seconds, the user sees a spinner replaced by the message: 'We could not process that right now. Your file is safe — try again in a moment.' A 'Try again' button appears. We do not show a stack trace, an error code, or the word 'error' anywhere on screen."

This describes what the user experiences. That is a user experience.

---

## Write It From the User's Perspective

Start your fallback UX description with: "The user sees..."

Then describe:
- What visual element appears (message, banner, highlighted field, modal)
- What the message says (write the actual words)
- What action the user can take next
- What is deliberately not shown (raw errors, technical language, AI uncertainty)

---

## Three Fallback Scenarios to Cover

Most products have at least two of these:

**Scenario A — API failure (network error, timeout, 500 from the model)**
What does the user see? Can they retry? Is their work lost?

**Scenario B — Low-confidence output**
What does the user see when the model is not sure? Is the output shown anyway with a warning? Is it hidden until reviewed?

**Scenario C — Content filter rejection (if your product uses generation)**
What does the user see when their prompt is rejected? Do you explain why? Do you suggest a rephrasing?

You do not need to cover all three — cover the ones relevant to your product. But cover at least one.

---

## The Confidence Threshold Pattern

If your product extracts structured data (fields from a document, entities from text, values from an image), this pattern earns the 3.0 score on Criterion 3:

- Results with confidence above [your threshold]: displayed directly
- Results with confidence between [lower] and [upper]: displayed with an amber highlight and a "Please verify" label
- Results with confidence below [lower]: shown as blank with a manual entry prompt

The specific thresholds are less important than having the pattern. Pick numbers and commit to them.
