# Week 2 Python — Theory & Computational Thinking Answers

- **Name:** Cherinet Kebede
- **Course:** Python Programming
- **Week:** 2

---

## 1. Core Python Logic & Decision Making

### Conditional Execution (`if`, `elif`, `else`)
- **Evaluation Mechanism:** Conditional statements check Boolean expressions sequentially from top to bottom. Once an expression evaluates to `True`, its corresponding indented block executes, and Python skips the remaining linked `elif` and `else` branches.
- **`if` vs. `elif` Behavior:**
  - Using an `elif` ensures that mutually exclusive conditions are evaluated together.
  - Using consecutive independent `if` statements forces the interpreter to check every single statement regardless of whether earlier ones matched, which can lead to redundant checks or unintended multiple outputs.

### Iteration Control (`for` vs. `while`)
- **`for` Loops (Definite Iteration):** Used when the range or collection of items to visit is established ahead of time (e.g., iterating through `range(1, N + 1)` in Task 08).
- **`while` Loops (Indefinite Iteration):** Used when the repetition depends on dynamic conditions that change at runtime, such as retrying user input until valid or until attempts run out (e.g., Task 07 guessing attempts or Task 09 PIN attempts).

---

## 2. Algorithmic Thinking & Task Breakdowns

### Task 03: Prime Number Checker & Optimization
- **Definition:** An integer greater than 1 with no positive divisors other than 1 and itself.
- **Handling Base Cases:**
  - `0` and `1` are not prime by definition.
  - `2` is prime (and the only even prime number).
- **Square-Root Factor Optimization:**
  - Divisors always pair up to equal the target number: $a \times b = N$.
  - If both factors were strictly greater than $\sqrt{N}$, their product would exceed $N$. Therefore, at least one factor in any valid pair must be less than or equal to $\sqrt{N}$.
  - By checking divisors only up to $\lfloor\sqrt{N}\rfloor$ (or $N // 2$ as a basic upper bound), we eliminate unnecessary operations, reducing time complexity from $O(N)$ down to $O(\sqrt{N})$.

---

### Task 05: Digit Summation via Arithmetic
- **String Conversion vs. Modulo/Division:**
  - Instead of casting an integer to a string and iterating over characters, pure numerical operations can extract digits directly.
  - **Extraction:** `num % 10` isolates the rightmost digit.
  - **Truncation:** `num // 10` removes the rightmost digit using integer division.
- **Loop Logic:** A `while num > 0:` loop continues stripping digits, adding each extracted value to a running accumulator until the number is reduced to 0.

---

### Task 08: Single-Pass Aggregation (Count Numbers)
- **Problem Breakdown:** Rather than iterating across the sequence multiple times to determine evens, odds, and totals independently, all three values are maintained concurrently.
- **Single-Loop Pattern:**
  1. Initialize `even_count = 0`, `odd_count = 0`, and `total_sum = 0`.
  2. Traverse each number $i$ from $1$ to $N$ in a single `for` loop.
  3. Add $i$ to `total_sum`.
  4. Evaluate `i % 2 == 0`: increment `even_count` if true; otherwise, increment `odd_count`.
- **Performance:** Completes in $O(N)$ runtime with $O(1)$ memory overhead.

---

### Task 09: ATM PIN Security & State Tracking
- **State Management:**
  - Configured constants: `CORRECT_PIN = "1234"` and `MAX_ATTEMPTS = 3`.
  - State tracking variables: `attempts_left = 3` and `is_authenticated = False`.
- **Control Flow:**
  - A `while` loop checks whether attempts remain and the user has not yet authenticated.
  - Correct input flips `is_authenticated` to `True` and exits the loop.
  - Incorrect input decrements `attempts_left` and displays the remaining balance of tries.
  - An exterior guard (`if not is_authenticated:`) triggers the account lockout message once the limit is exhausted.

---

### Task 10: Single-Pass Number Analyzer
- **Design Logic:**
  - Processes 10 sequential inputs within a single `for` loop, eliminating the need to store values in temporary lists or use multiple passes.
  - Initial state:
    - `total_sum = 0`
    - `even_count = 0`
    - `odd_count = 0`
    - `largest = None`
    - `smallest = None`
  - In each step:
    1. Read input integer.
    2. Add to `total_sum`.
    3. Update `even_count` or `odd_count` via `num % 2 == 0`.
    4. Update `largest` and `smallest` (using the first entered value as the baseline initializer).
  - Compute `average = total_sum / 10` after the loop terminates.

---

## 3. Computational Thinking Process

Applying structured computational thinking transforms broad prompts into stable implementations:

1. **Decomposition:** Splitting complex assignments (e.g., Task 10 or Bank Account systems) into atomic phases: user input, condition validation, variable mutations, and formatted reporting.
2. **Pattern Recognition:** Identifying that tasks like FizzBuzz, parity counting, and digit summation all rely on remainder arithmetic (`%`).
3. **Abstraction:** Isolating the core logic from cosmetic input strings so edge cases (such as negative inputs, 0, or matching boundaries) are handled uniformly.
4. **Algorithm Design:** Selecting appropriate constructs (e.g., single-pass loops, mathematical bounds) to optimize efficiency before writing the actual code.