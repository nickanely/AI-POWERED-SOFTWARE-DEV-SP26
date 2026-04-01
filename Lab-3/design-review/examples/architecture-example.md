# Example: Architecture Description

The example below is for a fictional EdTech tutoring app. Study the structure, then apply it to your own product.

---

## Sample Project: "StudyLens" — AI Homework Helper

StudyLens lets students photograph handwritten homework, ask a question about it, and receive a step-by-step explanation.

---

## Architecture Diagram Description

*(In your submission this would be an actual image — `architecture-diagram.png`. The text below describes what a correct diagram would contain for this project.)*

**Components in the diagram:**

```
[User's Browser]
       |
       | HTTPS (multipart form: image + question text)
       v
[FastAPI Backend — Railway, EU region]
       |                        |
       | base64 image +         | question text only
       | question text          |
       v                        v
[Gemini 3 Flash            [Supabase Postgres]
 via OpenRouter]            (stores session ID,
       |                    question, response —
       | JSON response       NOT the image)
       v
[FastAPI Backend]
       |
       | formatted explanation
       v
[User's Browser — renders step-by-step explanation]
```

**Key features of this diagram:**
- Frontend is labelled ("User's Browser")
- Backend is labelled with technology and host ("FastAPI Backend — Railway, EU region")
- AI model is named specifically ("Gemini 3 Flash via OpenRouter") — not just "AI"
- Storage is labelled with technology ("Supabase Postgres") and scope ("stores session ID, question, response — NOT the image")
- Arrows show direction of data flow
- The diagram makes clear that images are NOT stored (a deliberate privacy decision shown visually)

---

## Technology Stack Table (for DESIGN-REVIEW.md Section 4)

| Layer | Technology | Why |
|---|---|---|
| Frontend | React + Tailwind, deployed on Vercel | Fast iteration on UI, free hosting |
| Backend | FastAPI (Python) on Railway | Team knows Python from the labs, EU hosting for GDPR |
| Primary AI model | Gemini 3 Flash via OpenRouter | Free tier sufficient for demo, vision-capable |
| Secondary model (fallback) | GPT-4o mini via OpenRouter | Model swap requires one string change via OpenRouter |
| Storage | Supabase Postgres (EU) | Free tier, no images stored, only text logs |
| Hosting | Vercel (frontend) + Railway (backend) | Both have free tiers suitable for capstone |

---

## What a Weak Architecture Section Looks Like

**Wrong:**
"We will use Python for the backend and React for the frontend. The AI will process the user's homework photo and give an explanation."

This is 1.0 at best. It is prose. No diagram. No specific model named. No storage layer. No arrows.

**Right:** A committed PNG showing the five required components with labelled arrows.
