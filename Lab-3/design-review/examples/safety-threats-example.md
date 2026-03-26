# Example: Safety Threats

Filled threat table for StudyLens (the fictional EdTech tutoring app). Use this as a pattern for completing your own table — adapt the mitigations to your product, do not copy them verbatim.

---

## Filled Threat Table

| Threat | Relevant? | Mitigation |
|---|---|---|
| **Prompt injection** | Yes — students can type free-form questions that are inserted into our prompt. | User question text is inserted as a separate message content item, not concatenated into the system prompt string. System prompt is in a fixed system message that cannot be overwritten by user content. We length-limit user text to 500 characters. |
| **Hallucination in high-stakes output** | Partial — maths explanations are educational, not medical or financial. However, a wrong step explanation could entrench a student's misunderstanding. | The system prompt instructs the model to guide the student rather than give direct answers, reducing the impact of a hallucination on the final answer. We add a footer: "Always verify with your teacher." We do not present the tutor's output as authoritative. |
| **Bias affecting specific user groups** | Yes — model quality may vary for Georgian-language questions vs English-language questions. | We instruct the model to respond in the student's language. We will test the product with Georgian-language inputs before demo day and document any quality differences. If Georgian output is significantly weaker we will note it as a known limitation in the UI. |
| **Content policy violation** | Low — students upload photos of their own homework. Text input is a question about the homework. Unlikely to trigger content filters in normal use. | N/A for image generation (we do not generate images). For text: if the model refuses a student question, the soft-refusal fallback asks the student to rephrase. We log all refusals for review. |
| **Privacy violation** | Yes — students may upload photos that incidentally contain personal information (name on the worksheet, address on a letter used as backing paper). | We do not store uploaded images. Images are processed in memory, base64-encoded, sent to the API, and the encoded bytes are discarded after the response. We state this clearly in our privacy disclosure on the upload screen: "Your photo is sent to our AI for analysis and is not stored." |
| **Data exfiltration** | Low — our system has no multi-user data visible in the prompt. Each session is independent. | N/A — each API call contains only the current student's image and question. No other user data is in the prompt context. System prompt contains no secrets. We verify this in our session isolation tests. |

---

## Top Risk Statement

> Our biggest safety concern is **privacy violation**, because students may not realise their handwritten homework photos can contain personal information beyond the maths problem. We address this by not storing images and by showing a plain-language disclosure on the upload screen before they submit.

---

## What a Weak Safety Section Looks Like

**Wrong:**
"We will validate all inputs and handle errors securely. We will make sure our app is safe."

This scores 0. It names no specific threat. It describes no specific action. It is aspirational noise.

**Right:** The table above. Every row answered. Specific action for each relevant threat.
