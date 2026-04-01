# Example: Fallback UX

Two versions of the same product. One describes error handling code. One describes user experience. Only one scores 3.0.

---

## The Product: Receipt Expense Tracker

The app lets users photograph receipts and automatically extracts the amount, date, and vendor.

---

## Version A: Developer Framing (scores 1.0 at best)

> "We use try/except to catch API exceptions. If the vision API call fails, we return a 500 error to the frontend. We log the exception with the stack trace. If the confidence score is below our threshold, we set the field value to null and return an empty string to the frontend. The frontend checks for null and shows nothing."

**Why this fails:** The user has no idea what happened. "Nothing" appears on screen. There is no action they can take. "500 error" is a developer concept, not a user experience. The user's photo may have been lost.

---

## Version B: UX Framing (scores 3.0)

**Scenario: API call fails (timeout or server error)**

> The user sees a soft banner at the top of the results screen: "We had trouble reading that receipt — try again or enter the details manually." The upload area is still visible with their photo thumbnail. A "Try again" button re-submits the same photo. A "Enter manually" button opens a standard form with the three fields. The user's original photo is never lost — it stays visible throughout.

**Scenario: Low-confidence extraction (one or more fields uncertain)**

> Fields with high confidence (above 0.85) appear pre-filled with a green tick. Fields with medium confidence (0.60 to 0.85) appear pre-filled but highlighted in amber with the label "Please check this." Fields with low confidence (below 0.60) appear as empty input boxes with the placeholder "Could not read — please enter." The user can edit all fields before confirming. We never hide a low-confidence result without giving the user a way to fill it in themselves.

**Scenario: Content filter rejection (image flagged — rare but possible for images containing sensitive text)**

> The user sees: "We were unable to process that image. If it contains personal information like an ID or medical document, please remove or cover that section and try again." A "Try again" button appears. We do not use the words "content policy", "AI rejection", or "error".

---

## The Key Differences

| Developer framing | UX framing |
|---|---|
| Describes what the code does | Describes what the user sees |
| Uses technical language (500, null, exception) | Uses plain language |
| No user action available | Always gives the user a next step |
| The user may lose their work | The user's work is always visible and safe |
| "Error" is shown | "Error" is never shown to the user |

---

## Writing Yours

For each fallback scenario relevant to your product, complete this sentence:

"The user sees [visual element] with the message '[actual words]'. They can [action]. We do not show [what is deliberately hidden]."
