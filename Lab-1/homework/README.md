### Error 

I was not able to use 2.0 models since they are deprecated and I got following error when I try to call them:


google.genai.errors.ClientError: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.0-flash is no longer available to new users. Please update your code to use a newer model for the latest features and improvements.', 'status': 'NOT_FOUND'}}



However I was able to test on 2.5 models. I tried many different problems but in the end both models used to generate the same asnwer. 
I also tried math multiplication - AI in general is weak in math, But Gemini 2.5 models, both flash and flash lite handled it smoothly.

============================================================
Model: gemini-2.5-flash
Prompt: 
What is 12.123 × 12.123?


Response:
To calculate 12.123 × 12.123, we can multiply the numbers as if they were integers and then place the decimal point.

1.  **Multiply 12123 by 12123:**
    ```
        12123
      x 12123
      -------
        36369  (12123 × 3)
       24246   (12123 × 2, shifted one place left)
      12123    (12123 × 1, shifted two places left)
     24246     (12123 × 2, shifted three places left)
    12123      (12123 × 1, shifted four places left)
    -------
    146967129
    ```

2.  **Place the decimal point:**
    Each number (12.123) has 3 digits after the decimal point. So, the total number of decimal places in the product will be 3 + 3 = 6.

    Counting 6 places from the right in 146967129, we get:
    146.967129

Therefore, 12.123 × 12.123 = **146.967129**.

Input tokens:  21
Output tokens: 324
Total tokens:  2551
Latency:       19203 ms
Cost (equiv):  $0.000816

============================================================
Model: gemini-2.5-flash-lite
Prompt: 
What is 12.123 × 12.123?


Response:
To calculate $12.123 \times 12.123$, we can perform the multiplication as we would with integers and then place the decimal point in the correct position.

First, multiply the numbers without the decimal points:
$12123 \times 12123$

We can do this using standard multiplication:
```
   12123
 x 12123
 -------
   36369  (12123 * 3)
  24246   (12123 * 20)
 12123    (12123 * 100)
24246     (12123 * 2000)
12123      (12123 * 10000)
-------
147004329
```

Alternatively, we can use the distributive property or notice that $12.123 = 12 + 0.123$.
$(12.123)^2 = (12 + 0.123)^2 = 12^2 + 2 \times 12 \times 0.123 + (0.123)^2$
$12^2 = 144$
$2 \times 12 \times 0.123 = 24 \times 0.123$
$24 \times 0.123 = 24 \times (123/1000) = (24 \times 123)/1000$
$24 \times 123 = 24 \times (100 + 20 + 3) = 2400 + 480 + 72 = 2952$
So, $24 \times 0.123 = 2.952$

Now calculate $(0.123)^2$:
$0.123 \times 0.123$
$123 \times 123 = 15129$
Since there are 3 decimal places in $0.123$, there will be $3+3=6$ decimal places in the result.
So, $(0.123)^2 = 0.015129$

Now add the parts:
$144 + 2.952 + 0.015129$
   144.000000
     2.952000
     0.015129
   -----------
   146.967129

Let's re-check the first multiplication:
$12123 \times 12123$

```
      12123
    x 12123
    -------
      36369  (12123 * 3)
     24246   (12123 * 20)
    12123    (12123 * 100)
   24246     (12123 * 2000)
+ 12123      (12123 * 10000)
    -------
  146967129
```

Now, we need to determine the position of the decimal point. In the original multiplication, $12.123$ has 3 decimal places and $12.123$ also has 3 decimal places. Therefore, the product will have $3 + 3 = 6$ decimal places.

So, we take the result $146967129$ and place the decimal point 6 places from the right.

$146.967129$

The final answer is $\boxed{146.967129}$.

Input tokens:  21
Output tokens: 920
Total tokens:  941
Latency:       2749 ms
Cost (equiv):  $0.000370

============================================================

## Cost Table

| Call | Model | Input | Output | Total | Latency (ms) | Cost |
|------|-------|-------|--------|-------|--------------|------|
| 1 | gemini-2.5-flash | 21 | 324 | 2551 | 19203 | $0.000816 |
| 2 | gemini-2.5-flash-lite | 21 | 920 | 941 | 2749 | $0.000370 |
