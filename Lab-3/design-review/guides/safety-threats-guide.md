# Guide: Safety Threats

The Design Review requires you to name at least three safety threats relevant to your product and describe a specific mitigation for each. This is not a theoretical exercise — it is about your actual product.

---

## The Six Threats to Consider

**1. Prompt injection**
A user submits input that causes your system prompt to be overridden or ignored. For example, a user types "Ignore all previous instructions and tell me..." in a field your backend inserts directly into the prompt.

Is this relevant to you? Yes, if users can type free-form text that goes into your prompt.
Mitigation pattern: Sanitize user input before inserting into prompts. Use structured message formats that separate system instructions from user content. Never concatenate user text directly into a system prompt string.

**2. Hallucination in high-stakes output**
Your model returns a confident-sounding wrong answer in a context where being wrong matters — medical advice, legal interpretation, financial data.

Is this relevant to you? Yes, if your product makes claims about health, money, legal matters, or safety.
Mitigation pattern: Add confidence scoring. Route low-confidence outputs to human review or add a "verify with a professional" disclaimer. Never present AI output as authoritative in high-stakes domains.

**3. Bias affecting specific user groups**
Your model produces systematically different quality outputs for different users based on language, name, gender, or demographic signals in their input.

Is this relevant to you? Yes, for most products — especially those involving language, hiring, lending, or healthcare.
Mitigation pattern: Test your product with diverse inputs during development. Log and review cases where outputs differ unexpectedly. Note this as a known limitation in your UI where appropriate.

**4. Content policy violation**
Users submit prompts to image generation or text generation that trigger content filters, potentially exposing your application to misuse.

Is this relevant to you? Yes, if your product includes image generation or allows free-form user prompts to a generative model.
Mitigation pattern: Implement the content filter handler from Lab 3 Exercise 3. Log rejections. Show a clear, user-friendly fallback. Consider pre-screening user input with a moderation API before sending to the generative model.

**5. Privacy violation via logs or model memory**
User inputs containing personal data (names, health conditions, financial information) are stored in logs or sent to third-party APIs in ways users did not consent to.

Is this relevant to you? Yes, if users upload documents, images, or voice recordings containing personal information.
Mitigation pattern: Minimise what you log. Do not store full user inputs unless necessary. Check your API provider's data retention policy. Disclose in your UI what data is sent to which APIs.

**6. Data exfiltration**
A malicious user crafts a prompt that causes the model to reveal information it should not — another user's data, internal system prompts, or secrets.

Is this relevant to you? Yes, if your system has multi-user data or if your system prompt contains sensitive configuration.
Mitigation pattern: Never put secrets or other users' data in the system prompt. Validate that model responses do not contain internal system prompt text before displaying.

---

## How to Fill the Threat Table

For threats that apply: one sentence mitigation. Be specific about what your product will do.
For threats that do not apply: write "N/A — [one-sentence reason why]". Do not leave the cell blank.

A blank cell scores zero on that row. An "N/A" with a reason scores full marks for that row.
