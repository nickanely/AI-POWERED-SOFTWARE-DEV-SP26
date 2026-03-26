# Guide: Prompt and Data Flow

The data flow is different from the architecture diagram. The architecture shows what components exist. The data flow shows what happens — step by step — when a user takes one specific action.

---

## What to Trace

Pick the single most important AI feature in your product. Trace it from the moment the user acts to the moment they see a result.

Be specific. "The app calls the API" is not a step. "The backend constructs a system prompt containing the user's document text and sends it to Gemini 3 Flash via OpenRouter with a max token limit of 1024" is a step.

---

## The Seven Steps

Use these as your structure:

**1. User action**
What exactly does the user do? Click a button? Upload a file? Type a message? Submit a form?

**2. Preprocessing**
What happens to the user's input before any API call? Is an image resized? Is a document parsed to text? Is user context retrieved from the database?

**3. Prompt construction**
How is the prompt built? What is in the system prompt? How does the user's input get inserted? What other context is added (history, retrieved documents, instructions)?

**4. API call**
Which model? Via OpenRouter or direct? What parameters (temperature, max tokens, response format)?

**5. Response parsing**
What comes back from the API? Is it plain text? JSON? How do you extract the specific data you need from the full response?

**6. Confidence or validation**
How do you decide whether the response is good enough to show? Do you check a confidence field? Do you check for hallucination markers? Do you always show it?

**7. User output**
What does the user actually see on screen? And what do they see if step 6 fails — what is the fallback path?

---

## Common Mistakes

**Stopping at the API call:** Many teams write "we call the API and display the result". This skips steps 5, 6, and 7 which are the ones that determine whether your product is reliable.

**Describing features instead of data:** "Our app extracts invoice fields" is a feature. "The backend sends the invoice image as a base64-encoded string inside the user message content array, with a system prompt instructing the model to return a JSON object with keys amount, date, and vendor" is a data flow.

**Using "the AI" as a black box:** Name the model. Name the input format. Name the output format. The grader should be able to read your data flow and reproduce your API call.
