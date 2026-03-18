import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
]

# Paid-tier pricing per million tokens (input / output)
PRICING = {
    "gemini-2.5-flash":      (0.30, 2.50),
    "gemini-2.5-flash-lite": (0.10, 0.40),
}

PROMPT = (
"""
What is 12.123 × 12.123?
"""
)

def cost(model, input_tokens, output_tokens):
    in_price, out_price = PRICING.get(model, (0, 0))
    return (input_tokens * in_price + output_tokens * out_price) / 1_000_000

results = []

for model in MODELS:
    print(f"\n{'='*60}")
    print(f"Model: {model}")
    print(f"Prompt: {PROMPT}\n")

    start = time.time()
    response = client.models.generate_content(model=model, contents=PROMPT)
    latency_ms = (time.time() - start) * 1000

    usage = response.usage_metadata
    input_tokens  = usage.prompt_token_count
    output_tokens = usage.candidates_token_count
    total_tokens  = usage.total_token_count
    call_cost     = cost(model, input_tokens, output_tokens)

    print(f"Response:\n{response.text}")
    print(f"\nInput tokens:  {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    print(f"Total tokens:  {total_tokens}")
    print(f"Latency:       {latency_ms:.0f} ms")
    print(f"Cost (equiv):  ${call_cost:.6f}")

    results.append((model, input_tokens, output_tokens, total_tokens, latency_ms, call_cost))

# Print markdown table
print(f"\n{'='*60}")
print("## Cost Table\n")
print("| Call | Model | Input | Output | Total | Latency (ms) | Cost |")
print("|------|-------|-------|--------|-------|--------------|------|")
for i, (m, inp, out, tot, lat, c) in enumerate(results, 1):
    print(f"| {i} | {m} | {inp} | {out} | {tot} | {lat:.0f} | ${c:.6f} |")