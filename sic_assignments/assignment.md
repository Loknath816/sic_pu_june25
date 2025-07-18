
# Complete Solutions to Programming Assignments

## Git Operations

### 1. Add files in remote repo and also in local repo. Then sync them

#### Understanding the Problem:

- Need to add files both locally and remotely
- Synchronize changes between local and remote repositories

#### Solution:

```bash
# Add files locally
git add filename.txt
git commit -m "Add new file"

# Add files remotely (through GitHub web interface or another developer)
# Then sync:
git fetch origin
git merge origin/main
# Or simply:
git pull origin main

# Push local changes:
git push origin main
```

### 2. Learn to undo the 3 commands required to push (git add, git commit, git push)

#### Understanding the Problem:

- Undo git add, git commit, and git push operations
- Each has different implications and methods

#### Solution:

```bash
# Undo git add (unstage files)
git reset HEAD filename.txt
# Or for all files:
git reset HEAD

# Undo git commit (keep changes in working directory)
git reset --soft HEAD~1
# Or completely remove commit and changes:
git reset --hard HEAD~1

# Undo git push (dangerous - affects remote repository)
git reset --hard HEAD~1  # Remove commit locally
git push --force-with-lease origin main  # Force push (use with caution)
```

### 3. What happens when we have 2 commits and we try to push? Discuss in detail.

#### Understanding the Problem:

- Scenario with 2 local commits ready to push
- Understand the push process and potential conflicts

#### Solution:

When you have 2 commits and push:

1. **Normal Case (no conflicts):**
    
    ```bash
    git push origin main
    ```
    
    - Both commits are pushed to remote repository
    - Remote repository is updated with both commits
    - Local and remote are in sync
2. **Conflict Case (remote has newer commits):**
    
    ```bash
    git push origin main
    # Error: Updates were rejected because remote contains work
    ```
    
    - Must first pull remote changes
    - May require merge or rebase
    - Then push the merged result
3. **Resolution:**
    
    ```bash
    git pull origin main  # Fetch and merge
    git push origin main  # Now push works
    ```
    

## Memory and Language Concepts

### 4. How floating point number is stored in memory

#### Understanding the Problem:

- Understand IEEE 754 floating-point representation
- How decimal numbers are stored in binary format

#### Solution:

Floating-point numbers follow IEEE 754 standard:

**32-bit Float (Single Precision):**

- 1 bit: Sign (0 = positive, 1 = negative)
- 8 bits: Exponent (biased by 127)
- 23 bits: Mantissa (fractional part)

**64-bit Double (Double Precision):**

- 1 bit: Sign
- 11 bits: Exponent (biased by 1023)
- 52 bits: Mantissa

**Example:** 12.375 in float

- Binary: 1100.011
- Normalized: 1.100011 × 2³
- Sign: 0 (positive)
- Exponent: 3 + 127 = 130 = 10000010
- Mantissa: 10001100000000000000000

### 5. Find out why there are no ++ and -- operators in Python

#### Understanding the Problem:

- Python doesn't have increment/decrement operators
- Understand design philosophy behind this decision

#### Solution:

**Reasons why Python doesn't have ++ and --:**

1. **Integers are immutable:** `x++` would create a new integer object, not modify existing one
2. **Explicit is better than implicit:** Python philosophy favors clarity
3. **Avoid confusion:** No difference between `++x` and `x++` like in C/C++
4. **Consistency:** Python uses `x += 1` which works for all types

```python
# Instead of x++, use:
x += 1

# Instead of x--, use:
x -= 1

# Works with all types:
string += "text"
list += [item]
```

## Programming Problems

### 6. Check if a year is Leap year

#### Understanding the Problem:

- Determine if a given year is a leap year
- Follow leap year rules

#### Input/Output:

- Input: Year (integer)
- Output: Boolean (True/False)

#### Model the Solution:

Leap year rules:

1. Divisible by 4 AND
2. If divisible by 100, must also be divisible by 400

#### Edge Cases:

- Century years (1900, 2000)
- Negative years
- Year 0

#### Solution:

```python
def is_leap_year_brute_force(year):
    """
    Brute force approach: Check each condition separately
    Time: O(1), Space: O(1)
    """
    # Check if divisible by 4
    if year % 4 != 0:
        return False
    
    # Check if divisible by 100
    if year % 100 == 0:
        # If divisible by 100, check if divisible by 400
        if year % 400 == 0:
            return True
        else:
            return False
    
    # Divisible by 4 but not by 100
    return True

def is_leap_year_optimal(year):
    """
    Optimal approach: Single condition check
    Time: O(1), Space: O(1)
    """
    # Elegant one-liner using boolean logic
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Test cases
test_years = [2020, 2021, 1900, 2000, 2024]
for year in test_years:
    print(f"{year}: {is_leap_year_optimal(year)}")
```

### 7. Check if a +ve integer is Perfect square

#### Understanding the Problem:

- Determine if a positive integer is a perfect square
- A perfect square is n² for some integer n

#### Input/Output:

- Input: Positive integer
- Output: Boolean

#### Model the Solution:

1. Find square root and check if it's an integer
2. Or use binary search approach

#### Edge Cases:

- 0 and 1 (both perfect squares)
- Very large numbers

#### Solution:

```python
import math

def is_perfect_square_brute_force(n):
    """
    Brute force: Check all numbers from 1 to n
    Time: O(√n), Space: O(1)
    """
    if n < 0:
        return False
    
    if n == 0 or n == 1:
        return True
    
    # Check from 1 to n
    for i in range(1, n + 1):
        if i * i == n:
            return True
        if i * i > n:
            break
    
    return False

def is_perfect_square_optimal(n):
    """
    Optimal approach: Use math.sqrt
    Time: O(1), Space: O(1)
    """
    if n < 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def is_perfect_square_binary_search(n):
    """
    Binary search approach
    Time: O(log n), Space: O(1)
    """
    if n < 0:
        return False
    
    if n == 0 or n == 1:
        return True
    
    left, right = 1, n
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Test cases
test_numbers = [16, 17, 25, 26, 0, 1, 144, 145]
for num in test_numbers:
    print(f"{num}: {is_perfect_square_optimal(num)}")
```

### 8. Find smallest of 3 distinct numbers

#### Understanding the Problem:

- Find the minimum among three distinct numbers
- Numbers are guaranteed to be distinct

#### Input/Output:

- Input: Three distinct numbers
- Output: Smallest number

#### Model the Solution:

Compare numbers pairwise or use built-in functions

#### Edge Cases:

- Negative numbers
- Mixed positive/negative numbers

#### Solution:

```python
def find_smallest_brute_force(a, b, c):
    """
    Brute force: Multiple if-else conditions
    Time: O(1), Space: O(1)
    """
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

def find_smallest_optimal(a, b, c):
    """
    Optimal: Use built-in min function
    Time: O(1), Space: O(1)
    """
    return min(a, b, c)

def find_smallest_manual(a, b, c):
    """
    Manual approach without built-in functions
    Time: O(1), Space: O(1)
    """
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    return smallest

# Test cases
test_cases = [(5, 3, 8), (-2, 1, 0), (10, 20, 30), (-5, -10, -1)]
for a, b, c in test_cases:
    print(f"Smallest of {a}, {b}, {c}: {find_smallest_optimal(a, b, c)}")
```

### 9. Farmer Problem

#### Understanding the Problem:

- Classic problem: Farmer crossing river with fox, chicken, and grain
- Farmer can only take one item at a time
- Fox can't be alone with chicken, chicken can't be alone with grain

#### Input/Output:

- Input: Initial state (all on one side)
- Output: Sequence of moves to get all to other side

#### Model the Solution:

State-space search problem, can use BFS or provide step-by-step solution

#### Solution:

```python
def farmer_problem_solution():
    """
    Classic farmer problem solution
    F = Farmer, X = Fox, C = Chicken, G = Grain
    """
    print("Farmer Problem Solution:")
    print("Initial: [F, X, C, G] | []")
    
    steps = [
        ("Farmer takes Chicken", "[F, X, G] | [C]"),
        ("Farmer returns alone", "[X, G] | [F, C]"),
        ("Farmer takes Fox", "[G] | [F, X, C]"),
        ("Farmer returns with Chicken", "[F, C, G] | [X]"),
        ("Farmer takes Grain", "[F, C] | [X, G]"),
        ("Farmer returns alone", "[C] | [F, X, G]"),
        ("Farmer takes Chicken", "[] | [F, X, C, G]")
    ]
    
    for i, (action, state) in enumerate(steps, 1):
        print(f"Step {i}: {action}")
        print(f"State: {state}")
        print()

# More complex implementation with state representation
class FarmerState:
    def __init__(self, left_side, right_side):
        self.left = set(left_side)
        self.right = set(right_side)
    
    def is_valid(self):
        """Check if current state is valid"""
        # Check left side
        if 'F' not in self.left:
            if 'X' in self.left and 'C' in self.left:
                return False
            if 'C' in self.left and 'G' in self.left:
                return False
        
        # Check right side
        if 'F' not in self.right:
            if 'X' in self.right and 'C' in self.right:
                return False
            if 'C' in self.right and 'G' in self.right:
                return False
        
        return True
    
    def __str__(self):
        return f"{sorted(self.left)} | {sorted(self.right)}"

farmer_problem_solution()
```

### 10. Taxation problem

#### Understanding the Problem:

- Calculate tax based on income slabs
- Different tax rates for different income ranges

#### Input/Output:

- Input: Annual income
- Output: Tax amount

#### Model the Solution:

Progressive tax calculation with multiple slabs

#### Solution:

```python
def calculate_tax_brute_force(income):
    """
    Brute force: Check each slab individually
    Time: O(n) where n is number of slabs, Space: O(1)
    """
    tax = 0
    
    # Example tax slabs (Indian tax system)
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 250000 * 0.05 + (income - 500000) * 0.20
    else:
        tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30
    
    return tax

def calculate_tax_optimal(income):
    """
    Optimal: Use tax slab configuration
    Time: O(n), Space: O(1)
    """
    # Tax slabs: (upper_limit, rate)
    tax_slabs = [
        (250000, 0.0),
        (500000, 0.05),
        (1000000, 0.20),
        (float('inf'), 0.30)
    ]
    
    tax = 0
    prev_limit = 0
    
    for limit, rate in tax_slabs:
        if income <= prev_limit:
            break
        
        taxable_in_slab = min(income, limit) - prev_limit
        tax += taxable_in_slab * rate
        prev_limit = limit
    
    return tax

# Test cases
incomes = [200000, 300000, 600000, 1200000]
for income in incomes:
    tax = calculate_tax_optimal(income)
    print(f"Income: ₹{income:,}, Tax: ₹{tax:,.2f}")
```

## Python Module Functions

### Built-in Functions and Their Sources

#### Understanding the Problem:

- Identify which modules these functions come from
- Understand Python's built-in function system

#### Solution:

```python
# These functions are built-in functions, not from any module
# They are part of Python's __builtins__ module

def check_function_sources():
    """
    Check the sources of common Python functions
    """
    functions = {
        'range': 'Built-in function (no import needed)',
        'input': 'Built-in function (no import needed)',
        'print': 'Built-in function (no import needed)',
        'len': 'Built-in function (no import needed)',
        'min': 'Built-in function (no import needed)',
        'max': 'Built-in function (no import needed)',
        'sorted': 'Built-in function (no import needed)'
    }
    
    print("Function Sources:")
    for func, source in functions.items():
        print(f"{func}(): {source}")
    
    # Verify with __builtins__
    print(f"\nrange in __builtins__: {'range' in dir(__builtins__)}")
    print(f"input in __builtins__: {'input' in dir(__builtins__)}")

check_function_sources()
```

## Loop-based Problems

### 1. Find biggest digit in a number

#### Understanding the Problem:

- Extract each digit from a number
- Find the maximum digit

#### Input/Output:

- Input: Integer number
- Output: Largest digit

#### Model the Solution:

Extract digits using modulo and division operations

#### Edge Cases:

- Single digit numbers
- Negative numbers
- Zero

#### Solution:

```python
def find_biggest_digit_brute_force(n):
    """
    Brute force: Convert to string and iterate
    Time: O(d) where d is number of digits, Space: O(d)
    """
    if n < 0:
        n = -n  # Handle negative numbers
    
    n_str = str(n)
    max_digit = 0
    
    for digit_char in n_str:
        digit = int(digit_char)
        if digit > max_digit:
            max_digit = digit
    
    return max_digit

def find_biggest_digit_optimal(n):
    """
    Optimal: Use mathematical operations
    Time: O(d), Space: O(1)
    """
    if n < 0:
        n = -n  # Handle negative numbers
    
    max_digit = 0
    
    while n > 0:
        digit = n % 10
        max_digit = max(max_digit, digit)
        n //= 10
    
    return max_digit

# Test cases
test_numbers = [12345, 987654, 100, 7, -456]
for num in test_numbers:
    print(f"Biggest digit in {num}: {find_biggest_digit_optimal(num)}")
```

### 2. Find 2nd smallest digit in a number

#### Understanding the Problem:

- Find the second smallest unique digit in a number
- Handle cases where there might not be a second smallest

#### Input/Output:

- Input: Integer number
- Output: Second smallest digit or indication if doesn't exist

#### Model the Solution:

Collect all unique digits and sort them

#### Edge Cases:

- Numbers with less than 2 unique digits
- All digits are the same

#### Solution:

```python
def find_second_smallest_digit(n):
    """
    Find second smallest unique digit
    Time: O(d), Space: O(1) - at most 10 unique digits
    """
    if n < 0:
        n = -n
    
    # Collect unique digits
    digits = set()
    
    while n > 0:
        digits.add(n % 10)
        n //= 10
    
    # Convert to sorted list
    unique_digits = sorted(list(digits))
    
    if len(unique_digits) < 2:
        return None  # No second smallest digit
    
    return unique_digits[1]

# Test cases
test_numbers = [12345, 11111, 102, 7, 987654321]
for num in test_numbers:
    result = find_second_smallest_digit(num)
    if result is not None:
        print(f"Second smallest digit in {num}: {result}")
    else:
        print(f"No second smallest digit in {num}")
```

### 3. Count number of Prime digits in a number

#### Understanding the Problem:

- Count how many prime digits (2, 3, 5, 7) are in a number
- Prime digits are single-digit prime numbers

#### Input/Output:

- Input: Integer number
- Output: Count of prime digits

#### Model the Solution:

Check each digit if it's prime (2, 3, 5, 7)

#### Solution:

```python
def count_prime_digits(n):
    """
    Count prime digits in a number
    Time: O(d), Space: O(1)
    """
    if n < 0:
        n = -n
    
    prime_digits = {2, 3, 5, 7}
    count = 0
    
    while n > 0:
        digit = n % 10
        if digit in prime_digits:
            count += 1
        n //= 10
    
    return count

# Test cases
test_numbers = [12345, 2357, 1689, 777, 2222]
for num in test_numbers:
    print(f"Prime digits in {num}: {count_prime_digits(num)}")
```

### 4. Print Prime numbers in decreasing order between m and n (m < n)

#### Understanding the Problem:

- Find all prime numbers between m and n
- Print them in decreasing order

#### Input/Output:

- Input: Two integers m and n (m < n)
- Output: Prime numbers in decreasing order

#### Model the Solution:

1. Generate all primes in range using Sieve of Eratosthenes
2. Print in reverse order

#### Solution:

```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_decreasing_brute_force(m, n):
    """
    Brute force: Check each number for primality
    Time: O((n-m) * √n), Space: O(1)
    """
    primes = []
    
    for num in range(m, n + 1):
        if is_prime(num):
            primes.append(num)
    
    # Print in decreasing order
    for prime in reversed(primes):
        print(prime, end=" ")
    print()

def sieve_of_eratosthenes(n):
    """Generate all primes up to n using sieve"""
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i*i, n + 1, i):
                is_prime_arr[j] = False
    
    return is_prime_arr

def primes_decreasing_optimal(m, n):
    """
    Optimal: Use Sieve of Eratosthenes
    Time: O(n log log n), Space: O(n)
    """
    is_prime_arr = sieve_of_eratosthenes(n)
    primes = []
    
    for num in range(m, n + 1):
        if is_prime_arr[num]:
            primes.append(num)
    
    # Print in decreasing order
    for prime in reversed(primes):
        print(prime, end=" ")
    print()

# Test case
print("Primes between 10 and 30 in decreasing order:")
primes_decreasing_optimal(10, 30)
```

### 5. Find the Nth Fibonacci term (1st 2 terms are 1 and 2)

#### Understanding the Problem:

- Generate Fibonacci sequence where F(1)=1, F(2)=2
- Find the Nth term

#### Input/Output:

- Input: N (position in sequence)
- Output: Nth Fibonacci number

#### Model the Solution:

1. Iterative approach
2. Recursive approach (with memoization)

#### Solution:

```python
def fibonacci_brute_force(n):
    """
    Brute force recursive approach
    Time: O(2^n), Space: O(n)
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return fibonacci_brute_force(n-1) + fibonacci_brute_force(n-2)

def fibonacci_optimal(n):
    """
    Optimal iterative approach
    Time: O(n), Space: O(1)
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

def fibonacci_memoized(n, memo={}):
    """
    Memoized recursive approach
    Time: O(n), Space: O(n)
    """
    if n in memo:
        return memo[n]
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test cases
for i in range(1, 11):
    print(f"F({i}) = {fibonacci_optimal(i)}")
```

### 6. Find sum of series: n - n²/3 + n⁴/5 - n⁸/7 .... m terms

#### Understanding the Problem:

- Series: n - n²/3 + n⁴/5 - n⁸/7 + ...
- Pattern: alternating signs, powers of n (1,2,4,8...), denominators (1,3,5,7...)
- Calculate sum of m terms

#### Input/Output:

- Input: n (base number), m (number of terms)
- Output: Sum of m terms

#### Model the Solution:

1. Identify pattern: power doubles each term, denominator increases by 2
2. Alternate signs

#### Solution:

```python
def series_sum(n, m):
    """
    Calculate sum of series: n - n²/3 + n⁴/5 - n⁸/7 ....
    Time: O(m), Space: O(1)
    """
    total_sum = 0
    power = 1
    denominator = 1
    sign = 1
    
    for i in range(m):
        term = sign * (n ** power) / denominator
        total_sum += term
        
        # Update for next term
        power *= 2  # 1, 2, 4, 8, 16, ...
        denominator += 2  # 1, 3, 5, 7, 9, ...
        sign *= -1  # Alternate signs
    
    return total_sum

# Test cases
test_cases = [(2, 5), (3, 4), (1, 6)]
for n, m in test_cases:
    result = series_sum(n, m)
    print(f"Sum of series for n={n}, m={m}: {result:.4f}")
```

### 7. Print Pattern Shapes

#### Understanding the Problem:

- Print various geometric patterns
- Accept number of lines as input

#### Solutions for each pattern:

```python
def print_right_triangle(n):
    """
    Right Angled Triangle
    *
    **
    ***
    ****
    """
    for i in range(1, n + 1):
        print('*' * i)

def print_equilateral_triangle(n):
    """
    Equilateral Triangle
       *
      ***
     *****
    *******
    """
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def print_hollow_square(n):
    """
    Hollow Square
    ****
    *  *
    *  *
    ****
    """
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

def print_hollow_rhombus(n):
    """
    Hollow Rhombus
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
    """
    # Upper half including middle
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        if i == 0:
            print(spaces + '*')
        else:
            inner_spaces = ' ' * (2 * i - 1)
            print(spaces + '*' + inner_spaces + '*')
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        if i == 0:
            print(spaces + '*')
        else:
            inner_spaces = ' ' * (2 * i - 1)
            print(spaces + '*' + inner_spaces + '*')

def print_pascals_triangle(n):
    """
    Pascal's Triangle
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    """
    for i in range(n):
        # Calculate Pascal's triangle values
        row = [1]
        for j in range(1, i + 1):
            row.append(row[j-1] * (i - j + 1) // j)
        
        # Print with proper spacing
        spaces = ' ' * (n - i - 1)
        print(spaces + ' '.join(map(str, row)))

def print_x_shape(n):
    """
    X Shape
    *   *
     * *
      *
     * *
    *   *
    """
    for i in range(n):
        spaces = ' ' * i
        if i == n // 2:
            print(spaces + '*')
        else:
            inner_spaces = ' ' * (n - 2 * i - 2)
            if i < n // 2:
                print(spaces + '*' + inner_spaces + '*')
            else:
                spaces = ' ' * (n - i - 1)
                inner_spaces = ' ' * (2 * (i - n // 2) - 1)
                print(spaces + '*' + inner_spaces + '*')

# Test all patterns
n = 5
print("Right Triangle:")
print_right_triangle(n)
print("\nEquilateral Triangle:")
print_equilateral_triangle(n)
print("\nHollow Square:")
print_hollow_square(n)
print("\nPascal's Triangle:")
print_pascals_triangle(n)
```

### 8. Find sum of Even placed digits

#### Understanding the Problem:

- Sum digits at even positions (2nd, 4th, 6th position from right)
- Position counting starts from 1

#### Solution:

```python
def sum_even_placed_digits(n):
    """
    Sum of digits at even positions (from right, 1-indexed)
    Time: O(d), Space: O(1)
    """
    if n < 0:
        n = -n
    
    total = 0
    position = 1
    
    while n > 0:
        digit = n % 10
        if position % 2 == 0:  # Even position
            total += digit
        n //= 10
        position += 1
    
    return total

# Test cases
test_numbers = [12345, 987654, 13579, 2468]
for num in test_numbers:
    result = sum_even_placed_digits(num)
    print(f"Sum of even placed digits in {num}: {result}")
```

### 9. Find sum of Odd placed Even digits

#### Understanding the Problem:

- Find digits at odd positions that are even numbers
- Sum those digits

#### Solution:

````python
def sum_odd_placed_even_digits(n):
    """
    Sum of even digits at odd positions
    Time: O(d), Space: O(1)
    """
    if n < 0:
        n = -n
    
    total = 0
    position = 1
    
    while n > 0:
        digit = n % 10
        if position % 2 == 1 and digit % 2 == 0:  # Odd position and even digit
            total += digit
        n //= 10
        position += 1
    
    return total

# Test cases
test_numbers = [12345, 2468, 13579, 246810]
for num in test_numbers:
    result = sum_odd_placed_even_digits(num)
    print(f"Sum of odd placed even digits in {num}: {result}")

## Week 2 Problems

### 1. Ultimate Parent class in Python and its methods

#### Understanding the Problem:
- Identify the base class of all classes in Python
- List important methods and members

#### Solution:

```python
class ExampleClass:
    pass

# The ultimate parent class is 'object'
print(f"Base classes of ExampleClass: {ExampleClass.__bases__}")
print(f"MRO of ExampleClass: {ExampleClass.__mro__}")

# Important methods of object class
obj = ExampleClass()
print("\nImportant methods of object class:")
important_methods = [
    '__init__', '__new__', '__str__', '__repr__', '__eq__', '__ne__',
    '__hash__', '__bool__', '__getattribute__', '__setattr__', '__delattr__',
    '__dir__', '__class__', '__sizeof__', '__format__'
]

for method in important_methods:
    if hasattr(obj, method):
        print(f"  {method}: {getattr(obj, method)}")
````

### 2. Double underscore methods (dunder methods)

#### Understanding the Problem:

- Explain special methods in Python
- Show common dunder methods and their usage

#### Solution:

```python
class DunderExample:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"DunderExample({self.value})"
    
    def __repr__(self):
        return f"DunderExample(value={self.value})"
    
    def __add__(self, other):
        if isinstance(other, DunderExample):
            return DunderExample(self.value + other.value)
        return DunderExample(self.value + other)
    
    def __len__(self):
        return len(str(self.value))
    
    def __eq__(self, other):
        if isinstance(other, DunderExample):
            return self.value == other.value
        return self.value == other
    
    def __lt__(self, other):
        if isinstance(other, DunderExample):
            return self.value < other.value
        return self.value < other
    
    def __getitem__(self, key):
        return str(self.value)[key]
    
    def __call__(self, *args, **kwargs):
        return f"Called with args: {args}, kwargs: {kwargs}"

# Demonstrate dunder methods
obj1 = DunderExample(42)
obj2 = DunderExample(58)

print(f"str(obj1): {str(obj1)}")
print(f"repr(obj1): {repr(obj1)}")
print(f"obj1 + obj2: {obj1 + obj2}")
print(f"len(obj1): {len(obj1)}")
print(f"obj1 == obj2: {obj1 == obj2}")
print(f"obj1 < obj2: {obj1 < obj2}")
print(f"obj1[0]: {obj1[0]}")
print(f"obj1('hello'): {obj1('hello')}")
```

### 3. Define main function explicitly in Python

#### Understanding the Problem:

- Show how to define and use main function in Python
- Explain the if **name** == "**main**" pattern

#### Solution:

```python
def main():
    """
    Main function - entry point of the program
    """
    print("This is the main function")
    
    # Example of main function usage
    numbers = [1, 2, 3, 4, 5]
    result = process_numbers(numbers)
    print(f"Processed result: {result}")

def process_numbers(numbers):
    """Helper function called from main"""
    return sum(x * x for x in numbers)

def another_function():
    """Another helper function"""
    print("This is another function")

# This is the standard way to define main in Python
if __name__ == "__main__":
    main()
    
# Alternative explicit main definition
def explicit_main():
    """
    Explicit main function definition
    """
    import sys
    
    print("Program started")
    print(f"Command line arguments: {sys.argv}")
    
    # Your main program logic here
    try:
        # Main program execution
        result = perform_main_task()
        print(f"Main task result: {result}")
        return 0  # Success
    except Exception as e:
        print(f"Error: {e}")
        return 1  # Error

def perform_main_task():
    """Main task function"""
    return "Task completed successfully"

# Usage with explicit main
if __name__ == "__main__":
    import sys
    sys.exit(explicit_main())
```

### 4. List and String methods

#### Understanding the Problem:

- Enumerate important methods of list and str classes
- Show examples of their usage

#### Solution:

```python
def demonstrate_list_methods():
    """
    Demonstrate important list methods
    """
    print("=== LIST METHODS ===")
    
    # Create a sample list
    my_list = [1, 2, 3]
    
    # Modification methods
    my_list.append(4)                    # Add element at end
    print(f"After append(4): {my_list}")
    
    my_list.insert(1, 'inserted')        # Insert at specific position
    print(f"After insert(1, 'inserted'): {my_list}")
    
    my_list.extend([5, 6])               # Add multiple elements
    print(f"After extend([5, 6]): {my_list}")
    
    removed = my_list.remove('inserted') # Remove first occurrence
    print(f"After remove('inserted'): {my_list}")
    
    popped = my_list.pop()               # Remove and return last element
    print(f"After pop(): {my_list}, popped: {popped}")
    
    popped_index = my_list.pop(0)        # Remove and return element at index
    print(f"After pop(0): {my_list}, popped: {popped_index}")
    
    # Search methods
    my_list = [1, 2, 3, 2, 4, 2]
    print(f"index(2): {my_list.index(2)}")           # First occurrence
    print(f"count(2): {my_list.count(2)}")           # Count occurrences
    
    # Sorting methods
    my_list = [3, 1, 4, 1, 5, 9, 2, 6]
    my_list.sort()                       # Sort in place
    print(f"After sort(): {my_list}")
    
    my_list.reverse()                    # Reverse in place
    print(f"After reverse(): {my_list}")
    
    # Copy method
    list_copy = my_list.copy()           # Shallow copy
    print(f"copy(): {list_copy}")
    
    # Clear method
    temp_list = [1, 2, 3]
    temp_list.clear()                    # Remove all elements
    print(f"After clear(): {temp_list}")

def demonstrate_string_methods():
    """
    Demonstrate important string methods
    """
    print("\n=== STRING METHODS ===")
    
    # Case methods
    text = "Hello World Python"
    print(f"Original: '{text}'")
    print(f"upper(): '{text.upper()}'")
    print(f"lower(): '{text.lower()}'")
    print(f"capitalize(): '{text.capitalize()}'")
    print(f"title(): '{text.title()}'")
    print(f"swapcase(): '{text.swapcase()}'")
    
    # Search methods
    print(f"find('World'): {text.find('World')}")
    print(f"index('Python'): {text.index('Python')}")
    print(f"count('l'): {text.count('l')}")
    print(f"startswith('Hello'): {text.startswith('Hello')}")
    print(f"endswith('Python'): {text.endswith('Python')}")
    
    # Modification methods
    print(f"replace('World', 'Universe'): '{text.replace('World', 'Universe')}'")
    
    # Split and join methods
    words = text.split()
    print(f"split(): {words}")
    print(f"join with '-': '{'-'.join(words)}'")
    
    # Whitespace methods
    spaced_text = "   hello world   "
    print(f"strip(): '{spaced_text.strip()}'")
    print(f"lstrip(): '{spaced_text.lstrip()}'")
    print(f"rstrip(): '{spaced_text.rstrip()}'")
    
    # Checking methods
    print(f"isalpha(): {'hello'.isalpha()}")
    print(f"isdigit(): {'123'.isdigit()}")
    print(f"isalnum(): {'hello123'.isalnum()}")
    print(f"isspace(): {'   '.isspace()}")
    
    # Formatting methods
    template = "Hello, {}! You are {} years old."
    print(f"format(): '{template.format('Alice', 25)}'")
    
    # f-string alternative (Python 3.6+)
    name, age = "Bob", 30
    print(f"f-string: 'Hello, {name}! You are {age} years old.'")

# Run demonstrations
demonstrate_list_methods()
demonstrate_string_methods()
```

### 5. Why command line args are stored in list and not tuple?

#### Understanding the Problem:

- Explain why sys.argv is a list instead of tuple
- Discuss mutability vs immutability considerations

#### Solution:

```python
import sys

def explain_argv_as_list():
    """
    Explain why sys.argv is a list and not a tuple
    """
    print("=== WHY sys.argv IS A LIST ===")
    
    print("Current sys.argv:", sys.argv)
    print("Type of sys.argv:", type(sys.argv))
    
    print("\nReasons for using list over tuple:")
    
    print("1. MUTABILITY - Can modify command line arguments:")
    original_argv = sys.argv.copy()
    sys.argv.append("--additional-arg")
    print(f"   After append: {sys.argv}")
    sys.argv = original_argv  # Restore
    
    print("\n2. FLEXIBILITY - Can remove processed arguments:")
    if len(sys.argv) > 1:
        processed_arg = sys.argv.pop(1)
        print(f"   Processed and removed: {processed_arg}")
        print(f"   Remaining args: {sys.argv}")
        sys.argv.insert(1, processed_arg)  # Restore
    
    print("\n3. STANDARD LIBRARY CONSISTENCY:")
    print("   Most collections in Python are mutable by default")
    print("   Lists are more commonly used than tuples")
    
    print("\n4. ARGUMENT PARSING LIBRARIES:")
    print("   Libraries like argparse expect mutable sequences")
    print("   Easy to modify sys.argv before parsing")
    
    print("\n5. PERFORMANCE CONSIDERATIONS:")
    print("   Lists are optimized for append/pop operations")
    print("   Command line processing often involves modifications")

# Demonstrate argument processing
def process_arguments():
    """
    Example of how sys.argv mutability is useful
    """
    print("\n=== ARGUMENT PROCESSING EXAMPLE ===")
    
    # Simulate command line arguments
    simulated_argv = ['program.py', '--verbose', 'input.txt', '--output', 'output.txt']
    
    print(f"Original arguments: {simulated_argv}")
    
    # Process flags
    verbose = False
    if '--verbose' in simulated_argv:
        simulated_argv.remove('--verbose')
        verbose = True
    
    # Process named arguments
    output_file = None
    if '--output' in simulated_argv:
        idx = simulated_argv.index('--output')
        output_file = simulated_argv[idx + 1]
        # Remove both the flag and its value
        simulated_argv.pop(idx)  # Remove --output
        simulated_argv.pop(idx)  # Remove the value
    
    print(f"After processing: {simulated_argv}")
    print(f"Verbose mode: {verbose}")
    print(f"Output file: {output_file}")
    print(f"Remaining arguments: {simulated_argv[1:]}")  # Exclude program name

explain_argv_as_list()
process_arguments()
```

### 6. What is Pythonic and PEP 8?

#### Understanding the Problem:

- Explain Pythonic code philosophy
- Describe PEP 8 style guidelines

#### Solution:

````python
def explain_pythonic_and_pep8():
    """
    Explain Pythonic code and PEP 8 guidelines
    """
    print("=== PYTHONIC CODE ===")
    
    print("Pythonic code follows Python's philosophy:")
    print("- Simple is better than complex")
    print("- Readability counts")
    print("- Explicit is better than implicit")
    
    print("\n=== PEP 8 STYLE GUIDELINES ===")
    
    print("1. NAMING CONVENTIONS:")
    print("   - snake_case for variables and functions")
    print("   - PascalCase for classes")
    print("   - UPPER_CASE for constants")
    
    print("\n2. INDENTATION:")
    print("   - Use 4 spaces per indentation level")
    print("   - No tabs")
    
    print("\n3. LINE LENGTH:")
    print("   - Maximum 79 characters per line")
    print("   - 72 characters for comments and docstrings")
    
    print("\n4. IMPORTS:")
    print("   - One import per line")
    print("   - Standard library first, then third-party, then local")
    
    print("\n5. WHITESPACE:")
    print("   - Two blank lines before class and function definitions")
    print("   - One blank line between methods")

# Examples of Pythonic vs Non-Pythonic code
def pythonic_examples():
    """
    Examples of Pythonic code patterns
    """
    print("\n=== PYTHONIC EXAMPLES ===")
    
    # Example 1: List comprehension vs loop
    print("1. LIST COMPREHENSION:")
    numbers = [1, 2, 3, 4, 5]
    
    # Non-Pythonic
    squares_non_pythonic = []
    for num in numbers:
        squares_non_pythonic.append(num ** 2)
    
    # Pythonic
    squares_pythonic = [num ** 2 for num in numbers]
    
    print(f"   Non-Pythonic: {squares_non_pythonic}")
    print(f"   Pythonic: {squares_pythonic}")
    
    # Example 2: String formatting
    print("\n2. STRING FORMATTING:")
    name, age = "Alice", 25
    
    # Non-Pythonic
    message_non_pythonic = "Hello, " + name + "! You are " + str(age) + " years old."
    
    # Pythonic
    message_pythonic = f"Hello, {name}! You are {age} years old."
    
    print(f"   Non-Pythonic: {message_non_pythonic}")
    print(f"   Pythonic: {message_pythonic}")
    
    # Example 3: Dictionary access
    print("\n3. DICTIONARY ACCESS:")
    data = {"name": "Bob", "age": 30}
    
    # Non-Pythonic
    if "city" in data:
        city = data["city"]
    else:
        city = "Unknown"
    
    # Pythonic
    city_pythonic = data.get("city", "Unknown")
    
    print(f"   Non-Pythonic approach: {city}")
    print(f"   Pythonic approach: {city_pythonic}")
    
    # Example 4: Enumerate vs range(len())
    print("\n4. ENUMERATE:")
    items = ["apple", "banana", "cherry"]
    
    # Non-Pythonic
    print("   Non-Pythonic:")
    for i in range(len(items)):
        print(f"     {i}: {items[i]}")
    
    # Pythonic
    print("   Pythonic:")
    for i, item in enumerate(items):
        print(f"     {i}: {item}")

explain_pythonic_and_pep8()
pythonic_examples()

## DSA Problems

### 1. Binary Search using Recursion

#### Understanding the Problem:
- Implement binary search recursively
- Search for target in sorted array

#### Input/Output:
- Input: Sorted array and target value
- Output: Index of target or -1 if not found

#### Model the Solution:
Divide array in half, recursively search appropriate half

#### Edge Cases:
- Empty array
- Single element
- Target not in array

#### Solution:

```python
def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search implementation
    Time: O(log n), Space: O(log n) due to recursion stack
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    # Calculate middle index
    mid = (left + right) // 2
    
    # Element found
    if arr[mid] == target:
        return mid
    
    # Search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Search right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_iterative(arr, target):
    """
    Iterative binary search for comparison
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

# Test binary search
test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
test_targets = [7, 2, 19, 20]

print("Binary Search Results:")
for target in test_targets:
    result_recursive = binary_search_recursive(test_array, target)
    result_iterative = binary_search_iterative(test_array, target)
    print(f"Target {target}: Recursive={result_recursive}, Iterative={result_iterative}")
````

### 2. Fibonacci Series using Recursion

#### Understanding the Problem:

- Print N terms of Fibonacci series using recursion
- F(1)=1, F(2)=2 as given in problem

#### Solution:

```python
def print_fibonacci_recursive(n):
    """
    Print N terms of Fibonacci series using recursion
    Time: O(2^n), Space: O(n)
    """
    def fib(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return fib(n - 1) + fib(n - 2)
    
    print(f"First {n} Fibonacci terms:")
    for i in range(1, n + 1):
        print(fib(i), end=" ")
    print()

def print_fibonacci_optimized(n):
    """
    Optimized version using memoization
    Time: O(n), Space: O(n)
    """
    memo = {}
    
    def fib_memo(n):
        if n in memo:
            return memo[n]
        
        if n == 1:
            result = 1
        elif n == 2:
            result = 2
        else:
            result = fib_memo(n - 1) + fib_memo(n - 2)
        
        memo[n] = result
        return result
    
    print(f"First {n} Fibonacci terms (optimized):")
    for i in range(1, n + 1):
        print(fib_memo(i), end=" ")
    print()

# Test Fibonacci
print_fibonacci_recursive(10)
print_fibonacci_optimized(10)
```

### 3. Sum of digits using Recursion

#### Understanding the Problem:

- Calculate sum of digits in a number recursively
- Break down number digit by digit

#### Solution:

```python
def sum_of_digits_recursive(n):
    """
    Calculate sum of digits using recursion
    Time: O(log n), Space: O(log n)
    """
    # Base case
    if n == 0:
        return 0
    
    # Handle negative numbers
    if n < 0:
        n = -n
    
    # Recursive case: last digit + sum of remaining digits
    return (n % 10) + sum_of_digits_recursive(n // 10)

def sum_of_digits_iterative(n):
    """
    Iterative version for comparison
    Time: O(log n), Space: O(1)
    """
    if n < 0:
        n = -n
    
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    
    return total

# Test sum of digits
test_numbers = [123, 456, 789, 0, -123]
for num in test_numbers:
    recursive_result = sum_of_digits_recursive(num)
    iterative_result = sum_of_digits_iterative(num)
    print(f"Sum of digits in {num}: Recursive={recursive_result}, Iterative={iterative_result}")
```

### 4. Optimized Selection Sort

#### Understanding the Problem:

- Implement selection sort with optimizations
- Find minimum element and swap with first unsorted element

#### Solution:

```python
def selection_sort_basic(arr):
    """
    Basic selection sort implementation
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        # Find minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap found minimum element with first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return comparisons, swaps

def selection_sort_optimized(arr):
    """
    Optimized selection sort - find both min and max in each pass
    Time: O(n²), Space: O(1) - but with fewer comparisons
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    left = 0
    right = n - 1
    
    while left < right:
        min_idx = left
        max_idx = left
        
        # Find both minimum and maximum in current range
        for i in range(left + 1, right + 1):
            comparisons += 1
            if arr[i] < arr[min_idx]:
                min_idx = i
            
            comparisons += 1
            if arr[i] > arr[max_idx]:
                max_idx = i
        
        # Handle case where max is at the position where min will be placed
        if max_idx == left:
            max_idx = min_idx
        
        # Place minimum at left
        if min_idx != left:
            arr[left], arr[min_idx] = arr[min_idx], arr[left]
            swaps += 1
        
        # Place maximum at right
        if max_idx != right:
            arr[right], arr[max_idx] = arr[max_idx], arr[right]
            swaps += 1
        
        left += 1
        right -= 1
    
    return comparisons, swaps

# Test selection sort
test_array1 = [64, 34, 25, 12, 22, 11, 90]
test_array2 = test_array1.copy()

print("Original array:", test_array1)

comp1, swaps1 = selection_sort_basic(test_array1)
print(f"Basic selection sort: {test_array1}")
print(f"Comparisons: {comp1}, Swaps: {swaps1}")

comp2, swaps2 = selection_sort_optimized(test_array2)
print(f"Optimized selection sort: {test_array2}")
print(f"Comparisons: {comp2}, Swaps: {swaps2}")
```

### 5. Quick Sort Efficiency - Best Case

#### Understanding the Problem:

- Derive time complexity of Quick Sort for best case
- Best case occurs when pivot divides array into equal halves

#### Solution:

```python
def quicksort_with_analysis(arr, low=0, high=None):
    """
    Quick Sort implementation with operation counting
    """
    if high is None:
        high = len(arr) - 1
    
    operations = 0
    
    def partition(arr, low, high):
        nonlocal operations
        pivot = arr[high]  # Choose last element as pivot
        i = low - 1
        
        for j in range(low, high):
            operations += 1  # Comparison
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                operations += 1  # Swap
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        operations += 1  # Swap
        return i + 1
    
    def quicksort_helper(arr, low, high):
        nonlocal operations
        if low < high:
            pi = partition(arr, low, high)
            quicksort_helper(arr, low, pi - 1)
            quicksort_helper(arr, pi + 1, high)
    
    quicksort_helper(arr, low, high)
    return operations

def analyze_quicksort_best_case():
    """
    Analyze Quick Sort best case complexity
    """
    print("=== QUICK SORT BEST CASE ANALYSIS ===")
    
    print("Best case occurs when pivot always divides array into equal halves")
    print("\nRecurrence relation: T(n) = 2T(n/2) + O(n)")
    print("Where:")
    print("- 2T(n/2): Two recursive calls on half-sized arrays")
    print("- O(n): Partition operation")
    
    print("\nSolving using Master Theorem:")
    print("T(n) = 2T(n/2) + cn")
    print("a = 2, b = 2, f(n) = cn")
    print("log_b(a) = log_2(2) = 1")
    print("f(n) = cn = O(n¹)")
    print("Since f(n) = Θ(n^log_b(a)), we have Case 2")
    print("Therefore: T(n) = Θ(n log n)")
    
    # Empirical analysis
    print("\n=== EMPIRICAL ANALYSIS ===")
    import random
    
    sizes = [10, 50, 100, 500]
    for size in sizes:
        # Create best-case scenario (already sorted)
        arr = list(range(size))
        random.shuffle(arr)  # Shuffle to avoid worst-case
        
        operations = quicksort_with_analysis(arr.copy())
        theoretical = size * (size.bit_length() - 1)  # Approximation of n log n
        
        print(f"Size {size}: Operations={operations}, Theoretical≈{theoretical}")

analyze_quicksort_best_case()
```

### 6. Read-only variable in Python

#### Understanding the Problem:

- Python doesn't have true constants
- Show various ways to create read-only variables

#### Solution:

```python
# Method 1: Using property decorator
class ReadOnlyVariable:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    # No setter - makes it read-only

# Method 2: Using __slots__ and property
class ReadOnlyWithSlots:
    __slots__ = ['_value']
    
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value

# Method 3: Using namedtuple
from collections import namedtuple

ReadOnlyPoint = namedtuple('ReadOnlyPoint', ['x', 'y'])

# Method 4: Using __setattr__ override
class ReadOnlyClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)
        self._initialized = True
    
    def __setattr__(self, name, value):
        if hasattr(self, '_initialized'):
            raise AttributeError(f"Cannot modify read-only attribute '{name}'")
        super().__setattr__(name, value)

# Method 5: Using types.MappingProxyType for dictionaries
import types

def create_readonly_dict(d):
    return types.MappingProxyType(d)

# Method 6: Using frozen dataclass (Python 3.7+)
from dataclasses import dataclass

@dataclass(frozen=True)
class ReadOnlyDataClass:
    value: int
    name: str

# Demonstration
def demonstrate_readonly_variables():
    print("=== READ-ONLY VARIABLES IN PYTHON ===")
    
    # Method 1: Property
    print("1. Using property decorator:")
    ro_var = ReadOnlyVariable(42)
    print(f"   Value: {ro_var.value}")
    try:
        ro_var.value = 100  # This will fail
    except AttributeError as e:
        print(f"   Error: {e}")
    
    # Method 2: Namedtuple
    print("\n2. Using namedtuple:")
    point = ReadOnlyPoint(10, 20)
    print(f"   Point: {point}")
    try:
        point.x = 30  # This will fail
    except AttributeError as e:
        print(f"   Error: {e}")
    
    # Method 3: Read-only class
    print("\n3. Using __setattr__ override:")
    ro_obj = ReadOnlyClass(name="test", value=123)
    print(f"   Name: {ro_obj.name}, Value: {ro_obj.value}")
    try:
        ro_obj.name = "new_name"  # This will fail
    except AttributeError as e:
        print(f"   Error: {e}")
    
    # Method 4: MappingProxyType
    print("\n4. Using MappingProxyType:")
    original_dict = {"a": 1, "b": 2}
    readonly_dict = create_readonly_dict(original_dict)
    print(f"   Read-only dict: {readonly_dict}")
    try:
        readonly_dict["c"] = 3  # This will fail
    except TypeError as e:
        print(f"   Error: {e}")
    
    # Method 5
```

# Complete Python Solutions with Detailed Analysis

## 1. Read-Only Variables in Python

### Understanding the Problem

- **Goal**: Create variables that cannot be modified after initialization
- **Input**: Initial value for the variable
- **Output**: A variable that raises an error when modified
- **Model**: Use Python's property decorator or custom classes to restrict write access
- **Edge Cases**: Attempting to modify, delete, or reassign the variable

### Solution

```python
# Method 1: Using property decorator
class ReadOnlyVariable:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    # No setter defined - makes it read-only

# Method 2: Using __setattr__ to prevent modification
class ReadOnlyClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)
        self._initialized = True
    
    def __setattr__(self, name, value):
        if hasattr(self, '_initialized'):
            raise AttributeError(f"Cannot modify read-only attribute '{name}'")
        super().__setattr__(name, value)

# Method 3: Using namedtuple (immutable)
from collections import namedtuple

ReadOnlyData = namedtuple('ReadOnlyData', ['value'])

# Usage examples
print("Method 1: Property decorator")
var1 = ReadOnlyVariable(42)
print(f"Value: {var1.value}")
# var1.value = 50  # This would raise AttributeError

print("\nMethod 2: Custom __setattr__")
var2 = ReadOnlyClass(x=10, y=20)
print(f"x: {var2.x}, y: {var2.y}")
# var2.x = 15  # This would raise AttributeError

print("\nMethod 3: namedtuple")
var3 = ReadOnlyData(100)
print(f"Value: {var3.value}")
# var3.value = 200  # This would raise AttributeError
```

---

## 2. Queue Implementation using Singly Linked List (SLL) and Doubly Linked List (DLL)

### Understanding the Problem

- **Goal**: Implement queue operations (enqueue, dequeue) with insert at rear and delete from front
- **Input**: Elements to be added/removed from queue
- **Output**: Queue with FIFO behavior
- **Model**: Use linked list structure with pointers to front and rear
- **Edge Cases**: Empty queue dequeue, single element queue

### Solution

```python
# Singly Linked List Implementation
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingSLL:
    def __init__(self):
        self.front = None  # Points to first element (for deletion)
        self.rear = None   # Points to last element (for insertion)
        self.size = 0
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return self.front is None
    
    def enqueue(self, data):
        """Insert at rear - O(1)"""
        new_node = SLLNode(data)
        
        if self.is_empty():
            # First element - both front and rear point to it
            self.front = self.rear = new_node
        else:
            # Add to rear and update rear pointer
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        """Delete from front - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        # If queue becomes empty, update rear to None
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        print(f"Dequeued: {data}")
        return data
    
    def peek(self):
        """Get front element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
    
    def display(self):
        """Display all elements - O(n)"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue: " + " -> ".join(elements))

# Doubly Linked List Implementation
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class QueueUsingDLL:
    def __init__(self):
        self.front = None  # Points to first element
        self.rear = None   # Points to last element
        self.size = 0
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return self.front is None
    
    def enqueue(self, data):
        """Insert at rear - O(1)"""
        new_node = DLLNode(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            # Link new node to current rear
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        """Delete from front - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front:
            self.front.prev = None
        else:
            # Queue becomes empty
            self.rear = None
        
        self.size -= 1
        print(f"Dequeued: {data}")
        return data
    
    def peek(self):
        """Get front element - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
    
    def display(self):
        """Display all elements - O(n)"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue: " + " -> ".join(elements))

# Test both implementations
print("=== Queue using Singly Linked List ===")
sll_queue = QueueUsingSLL()
sll_queue.enqueue(10)
sll_queue.enqueue(20)
sll_queue.enqueue(30)
sll_queue.display()
sll_queue.dequeue()
sll_queue.display()

print("\n=== Queue using Doubly Linked List ===")
dll_queue = QueueUsingDLL()
dll_queue.enqueue(10)
dll_queue.enqueue(20)
dll_queue.enqueue(30)
dll_queue.display()
dll_queue.dequeue()
dll_queue.display()
```

---

## 3. Stack Implementation using SLL and DLL

### Understanding the Problem

- **Goal**: Implement stack operations (push, pop) with LIFO behavior
- **Input**: Elements to be added/removed from stack
- **Output**: Stack with LIFO behavior
- **Model**: Use linked list with operations at one end (top)
- **Edge Cases**: Empty stack pop, single element stack

### Solution

```python
# Stack using Singly Linked List
class StackUsingSLL:
    def __init__(self):
        self.top = None  # Points to top element
        self.size = 0
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return self.top is None
    
    def push(self, data):
        """Insert at front (top) - O(1)"""
        new_node = SLLNode(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Pushed: {data}")
    
    def pop(self):
        """Delete from front (top) - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Popped: {data}")
        return data
    
    def peek(self):
        """Get top element - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data
    
    def display(self):
        """Display all elements - O(n)"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Stack (top to bottom): " + " -> ".join(elements))

# Stack using Doubly Linked List
class StackUsingDLL:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return self.top is None
    
    def push(self, data):
        """Insert at front (top) - O(1)"""
        new_node = DLLNode(data)
        if not self.is_empty():
            new_node.next = self.top
            self.top.prev = new_node
        self.top = new_node
        self.size += 1
        print(f"Pushed: {data}")
    
    def pop(self):
        """Delete from front (top) - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        if self.top:
            self.top.prev = None
        
        self.size -= 1
        print(f"Popped: {data}")
        return data
    
    def peek(self):
        """Get top element - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data
    
    def display(self):
        """Display all elements - O(n)"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Stack (top to bottom): " + " -> ".join(elements))

# Test both implementations
print("=== Stack using Singly Linked List ===")
sll_stack = StackUsingSLL()
sll_stack.push(10)
sll_stack.push(20)
sll_stack.push(30)
sll_stack.display()
sll_stack.pop()
sll_stack.display()

print("\n=== Stack using Doubly Linked List ===")
dll_stack = StackUsingDLL()
dll_stack.push(10)
dll_stack.push(20)
dll_stack.push(30)
dll_stack.display()
dll_stack.pop()
dll_stack.display()
```

---

## 4. Reverse a Singly Linked List

### Understanding the Problem

- **Goal**: Reverse the order of nodes in a singly linked list
- **Input**: Head of original linked list
- **Output**: Head of reversed linked list
- **Model**: Change direction of pointers or use recursion
- **Edge Cases**: Empty list, single node, two nodes

### Solution

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def display_list(head):
    """Helper function to display linked list"""
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    return " -> ".join(elements)

def create_list(values):
    """Helper function to create linked list from values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Brute Force Approach: Using extra space
def reverse_list_brute_force(head):
    """
    Brute Force: Store values in array, then rebuild list
    Time: O(n), Space: O(n)
    """
    if not head:
        return None
    
    # Store all values in array
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Rebuild list in reverse order
    new_head = ListNode(values[-1])
    current = new_head
    for i in range(len(values) - 2, -1, -1):
        current.next = ListNode(values[i])
        current = current.next
    
    return new_head

# Optimal Approach 1: Iterative pointer reversal
def reverse_list_iterative(head):
    """
    Optimal: Reverse pointers iteratively
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        # Store next node before breaking the link
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # prev is now the new head
    return prev

# Optimal Approach 2: Recursive
def reverse_list_recursive(head):
    """
    Optimal: Reverse using recursion
    Time: O(n), Space: O(n) due to recursion stack
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return new_head

# Test all approaches
print("=== Reverse Singly Linked List ===")
original_values = [1, 2, 3, 4, 5]
print(f"Original: {original_values}")

# Test brute force
head1 = create_list(original_values)
print(f"Before reverse: {display_list(head1)}")
reversed_head1 = reverse_list_brute_force(head1)
print(f"After reverse (brute force): {display_list(reversed_head1)}")

# Test iterative
head2 = create_list(original_values)
reversed_head2 = reverse_list_iterative(head2)
print(f"After reverse (iterative): {display_list(reversed_head2)}")

# Test recursive
head3 = create_list(original_values)
reversed_head3 = reverse_list_recursive(head3)
print(f"After reverse (recursive): {display_list(reversed_head3)}")
```

---

## 5. Merge Two Sorted Singly Linked Lists

### Understanding the Problem

- **Goal**: Merge two sorted linked lists into one sorted list
- **Input**: Two sorted linked list heads
- **Output**: Head of merged sorted linked list
- **Model**: Compare nodes and link smaller ones first
- **Edge Cases**: Empty lists, lists of different lengths, duplicate values

### Solution

```python
# Brute Force Approach: Collect all values and sort
def merge_lists_brute_force(list1, list2):
    """
    Brute Force: Collect all values, sort, and rebuild
    Time: O(n log n), Space: O(n)
    """
    values = []
    
    # Collect all values from both lists
    current = list1
    while current:
        values.append(current.val)
        current = current.next
    
    current = list2
    while current:
        values.append(current.val)
        current = current.next
    
    # Sort values
    values.sort()
    
    # Rebuild sorted list
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Optimal Approach 1: Iterative merge
def merge_lists_iterative(list1, list2):
    """
    Optimal: Merge using two pointers
    Time: O(n + m), Space: O(1)
    """
    # Create dummy head to simplify logic
    dummy = ListNode(0)
    current = dummy
    
    # Compare and merge while both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes (one list is exhausted)
    current.next = list1 if list1 else list2
    
    return dummy.next

# Optimal Approach 2: Recursive merge
def merge_lists_recursive(list1, list2):
    """
    Optimal: Merge using recursion
    Time: O(n + m), Space: O(n + m) due to recursion stack
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Choose smaller node and recursively merge rest
    if list1.val <= list2.val:
        list1.next = merge_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_lists_recursive(list1, list2.next)
        return list2

# Test all approaches
print("\n=== Merge Two Sorted Lists ===")
list1_values = [1, 2, 4, 7]
list2_values = [1, 3, 4, 6, 8]

print(f"List 1: {list1_values}")
print(f"List 2: {list2_values}")

# Test brute force
head1 = create_list(list1_values)
head2 = create_list(list2_values)
merged_brute = merge_lists_brute_force(head1, head2)
print(f"Merged (brute force): {display_list(merged_brute)}")

# Test iterative
head1 = create_list(list1_values)
head2 = create_list(list2_values)
merged_iterative = merge_lists_iterative(head1, head2)
print(f"Merged (iterative): {display_list(merged_iterative)}")

# Test recursive
head1 = create_list(list1_values)
head2 = create_list(list2_values)
merged_recursive = merge_lists_recursive(head1, head2)
print(f"Merged (recursive): {display_list(merged_recursive)}")
```

---

## 6. Check if Two Singly Linked Lists Converge

### Understanding the Problem

- **Goal**: Determine if two linked lists intersect at some point
- **Input**: Two linked list heads
- **Output**: Boolean indicating if they converge, optionally the intersection node
- **Model**: Use hash set or two-pointer technique
- **Edge Cases**: No intersection, same lists, different lengths

### Solution

```python
# Brute Force Approach: Check every pair of nodes
def lists_converge_brute_force(head1, head2):
    """
    Brute Force: Compare every node in list1 with every node in list2
    Time: O(n * m), Space: O(1)
    """
    if not head1 or not head2:
        return False
    
    current1 = head1
    while current1:
        current2 = head2
        while current2:
            # Compare node references (not values)
            if current1 is current2:
                return True
            current2 = current2.next
        current1 = current1.next
    
    return False

# Better Approach: Using hash set
def lists_converge_hash_set(head1, head2):
    """
    Using hash set to store visited nodes
    Time: O(n + m), Space: O(n)
    """
    if not head1 or not head2:
        return False
    
    # Store all nodes from first list
    visited = set()
    current = head1
    while current:
        visited.add(current)
        current = current.next
    
    # Check if any node in second list is visited
    current = head2
    while current:
        if current in visited:
            return True
        current = current.next
    
    return False

# Optimal Approach: Two pointers technique
def lists_converge_optimal(head1, head2):
    """
    Two pointers: Each pointer traverses both lists
    Time: O(n + m), Space: O(1)
    """
    if not head1 or not head2:
        return False
    
    # Two pointers starting from different heads
    ptr1, ptr2 = head1, head2
    
    # Continue until they meet or both reach end
    while ptr1 != ptr2:
        # When ptr1 reaches end, start from head2
        ptr1 = head2 if ptr1 is None else ptr1.next
        # When ptr2 reaches end, start from head1
        ptr2 = head1 if ptr2 is None else ptr2.next
    
    # If they converge, ptr1 == ptr2 (intersection node)
    # If no intersection, both will be None
    return ptr1 is not None

# Function to find intersection node (not just check convergence)
def find_intersection_node(head1, head2):
    """
    Find the actual intersection node
    Time: O(n + m), Space: O(1)
    """
    if not head1 or not head2:
        return None
    
    ptr1, ptr2 = head1, head2
    
    while ptr1 != ptr2:
        ptr1 = head2 if ptr1 is None else ptr1.next
        ptr2 = head1 if ptr2 is None else ptr2.next
    
    return ptr1  # Returns intersection node or None

# Helper function to create intersecting lists
def create_intersecting_lists():
    """Create two lists that intersect for testing"""
    # Create common part: 8 -> 4 -> 5
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    # Create list1: 4 -> 1 -> 8 -> 4 -> 5
    list1 = ListNode(4)
    list1.next = ListNode(1)
    list1.next.next = common
    
    # Create list2: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(1)
    list2.next.next.next = common
    
    return list1, list2

# Test convergence detection
print("\n=== Check if Lists Converge ===")

# Test with intersecting lists
list1, list2 = create_intersecting_lists()
print(f"List 1: {display_list(list1)}")
print(f"List 2: {display_list(list2)}")

print(f"Converge (brute force): {lists_converge_brute_force(list1, list2)}")
print(f"Converge (hash set): {lists_converge_hash_set(list1, list2)}")
print(f"Converge (optimal): {lists_converge_optimal(list1, list2)}")

intersection = find_intersection_node(list1, list2)
print(f"Intersection node value: {intersection.val if intersection else None}")

# Test with non-intersecting lists
list3 = create_list([1, 2, 3])
list4 = create_list([4, 5, 6])
print(f"\nNon-intersecting lists:")
print(f"List 3: {display_list(list3)}")
print(f"List 4: {display_list(list4)}")
print(f"Converge (optimal): {lists_converge_optimal(list3, list4)}")
```

---

## 7. Circular Queue Implementation using Array/List

### Understanding the Problem

- **Goal**: Implement a circular queue with fixed size using array
- **Input**: Maximum size of queue and elements to enqueue/dequeue
- **Output**: Circular queue with efficient space utilization
- **Model**: Use array with front and rear pointers that wrap around
- **Edge Cases**: Queue full, queue empty, single element

### Solution

```python
# Brute Force Approach: Using dynamic list (not truly circular)
class CircularQueueBruteForce:
    """
    Brute Force: Use list with shifting elements
    Time: O(n) for dequeue, O(1) for enqueue
    Space: O(n)
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.capacity
    
    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.queue.append(data)
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        # O(n) operation - all elements shift
        data = self.queue.pop(0)
        print(f"Dequeued: {data}")
        return data
    
    def display(self):
        print(f"Queue: {self.queue}")

# Optimal Approach: True circular queue with fixed array
class CircularQueueOptimal:
    """
    Optimal: Use fixed array with circular indexing
    Time: O(1) for all operations
    Space: O(n) where n is capacity
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of front element
        self.rear = -1   # Index of rear element
        self.size = 0    # Current number of elements
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.size == 0
    
    def is_full(self):
        """Check if queue is full"""
        return self.size == self.capacity
    
    def enqueue(self, data):
        """Add element to rear - O(1)"""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        if self.is_empty():
            # First element
            self.front = self.rear = 0
        else:
            # Move rear in circular manner
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = data
        self.size += 1
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        """Remove element from front - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot
        
        if self.size == 1:
            # Last element - reset pointers
            self.front = self.rear = -1
        else:
            # Move front in circular manner
            self.front = (self.front + 1) % self.capacity
        
        self.size -= 1
        print(f"Dequeued: {data}")
        return data
    
    def peek(self):
        """Get front element without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    
    def display(self):
        """Display queue elements"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        elements = []
        i = self.front
        for _ in range(self.size):
            elements.append(str(self.queue[i]))
            i = (i + 1) % self.capacity
        
        print(f"Queue: [{', '.join(elements)}]")
        print(f"Front: {self.front}, Rear: {self.rear}, Size: {self.size}")

# Alternative implementation using different logic
class CircularQueueAlternative:
    """
    Alternative: Use (rear + 1) % capacity == front to detect full
    Sacrifices one slot to distinguish between full and empty
    """
    def __init__(self, capacity):
        self.capacity = capacity + 1  # One extra slot
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        print(f"Dequeued: {data}")
        return data
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        elements = []
        i = self.front
        while i != self.rear:
            elements.append(str(self.queue[i]))
            i = (i + 1) % self.capacity
        
        print(f"Queue: [{', '.join(elements)}]")

# Test all implementations
print("\n=== Circular Queue Implementations ===")

# Test optimal implementation
print("Optimal Circular Queue:")
cq = CircularQueueOptimal(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
cq.dequeue()
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)
cq.display()
cq.dequeue()
cq.dequeue()
cq.display()

print("\nAlternative Implementation:")
cq2 = CircularQueueAlternative(5)
cq2.enqueue(10)
cq2.enqueue(20)
cq2.enqueue(30)
cq2.display()
cq2.dequeue()
cq2.enqueue(40)
cq2.display()
```

---

## 8. Matrix Spiral Print

### Understanding the Problem

- **Goal**: Print matrix elements in spiral order (clockwise from outside to inside)
- **Input**: 2D matrix of size M x N
- **Output**: Elements printed in spiral order
- **Model**: Use four boundaries (top, bottom, left, right) and move in spiral pattern
- **Edge Cases**: Single row, single column, empty matrix, square matrix

### Solution

```python
# Brute Force Approach: Create visited matrix
def print_spiral_brute_force(matrix):
    """
    Brute Force: Use visited matrix to track covered cells
    Time: O(m*n), Space: O(m*n)
    """
    if not matrix or not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    result = []
    
    # Direction vectors: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0
    
    row, col = 0, 0
    
    for _ in range(m * n):
        result.append(matrix[row][col])
        visited[row][col] = True
        
        # Calculate next position
        next_row = row + directions[current_dir][0]
        next_col = col + directions[current_dir][1]
        
        # Check if we need to turn (hit boundary or visited cell)
        if (next_row < 0 or next_row >= m or 
            next_col < 0 or next_col >= n or 
            visited[next_row][next_col]):
            # Turn clockwise
            current_dir = (current_dir + 1) % 4
            next_row = row + directions[current_dir][0]
            next_col = col + directions[current_dir][1]
        
        row, col = next_row, next_col
    
    return result

# Optimal Approach: Layer by layer traversal
def print_spiral_optimal(matrix):
    """
    Optimal: Use four boundaries and shrink them
    Time: O(m*n), Space: O(1) - not counting output
    """
    if not matrix or not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    
    # Define boundaries
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # Traverse right along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Traverse left along bottom row (if still valid)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Traverse up along left column (if still valid)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# Function to print matrix in readable format
def print_matrix(matrix):
    """Helper function to display matrix"""
    for row in matrix:
        print([f"{cell:3}" for cell in row])

# Test both approaches
print("\n=== Matrix Spiral Print ===")

# Test case 1: Regular matrix
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Matrix 1:")
print_matrix(matrix1)
print(f"Spiral (brute force): {print_spiral_brute_force(matrix1)}")
print(f"Spiral (optimal): {print_spiral_optimal(matrix1)}")

# Test case 2: Single row
matrix2 = [[1, 2, 3, 4, 5]]
print(f"\nSingle row: {matrix2}")
print(f"Spiral (optimal): {print_spiral_optimal(matrix2)}")

# Test case 3: Single column
matrix3 = [[1], [2], [3], [4]]
print(f"\nSingle column: {matrix3}")
print(f"Spiral (optimal): {print_spiral_optimal(matrix3)}")

# Test case 4: Non-square matrix
matrix4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(f"\nNon-square matrix:")
print_matrix(matrix4)
print(f"Spiral (optimal): {print_spiral_optimal(matrix4)}")
```

---

## Additional Data Structure Problems

### Understanding Tree Problems

- **Goal**: Implement various tree data structures and operations
- **Input**: Tree nodes with parent-child relationships
- **Output**: Tree with specific properties (BST, AVL, etc.)
- **Model**: Use recursive structure with left and right children
- **Edge Cases**: Empty tree, single node, unbalanced tree

### BST (Binary Search Tree) Implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert value into BST - O(log n) average, O(n) worst"""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        # Base case: create new node
        if not node:
            return TreeNode(val)
        
        # Insert in appropriate subtree
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val):
        """Search for value in BST - O(log n) average, O(n) worst"""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def inorder_traversal(self):
        """Inorder traversal gives sorted order - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def delete(self, val):
        """Delete value from BST - O(log n) average, O(n) worst"""
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node to be deleted found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node has two children: find inorder successor
            successor = self._find_min(node.right)
            node.val = successor.val
            node.right = self._delete_recursive(node.right, successor.val)
        
        return node
    
    def _find_min(self, node):
        """Find minimum value node in subtree"""
        while node.left:
            node = node.left
        return node

# Test BST
print("\n=== Binary Search Tree ===")
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for val in values:
    bst.insert(val)

print(f"Inserted values: {values}")
print(f"Inorder traversal: {bst.inorder_traversal()}")
print(f"Search for 40: {'Found' if bst.search(40) else 'Not found'}")
print(f"Search for 90: {'Found' if bst.search(90) else 'Not found'}")

bst.delete(30)
print(f"After deleting 30: {bst.inorder_traversal()}")
```

---

### Sorting Algorithms Implementation

```python
import random
import time

# Bubble Sort - Brute Force
def bubble_sort(arr):
    """
    Bubble Sort: Compare adjacent elements and swap
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr

# Merge Sort - Optimal for comparison-based sorting
def merge_sort(arr):
    """
    Merge Sort: Divide and conquer approach
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Quick Sort - Average case optimal
def quick_sort(arr):
    """
    Quick Sort: Partition around pivot
    Time: O(n log n) average, O(n²) worst, Space: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Heap Sort - Guaranteed O(n log n)
def heap_sort(arr):
    """
    Heap Sort: Build max heap and extract elements
    Time: O(n log n), Space: O(1)
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """Maintain heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Radix Sort - Non-comparison based
def radix_sort(arr):
    """
    Radix Sort: Sort by individual digits
    Time: O(d * n), Space: O(n + k)
    """
    if not arr:
        return arr
    
    # Find maximum number to determine number of digits
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_for_radix(arr, exp):
    """Counting sort for radix sort"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]

# Test all sorting algorithms
print("\n=== Sorting Algorithms Comparison ===")
test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
print(f"Original array: {test_array}")

print(f"Bubble Sort: {bubble_sort(test_array)}")
print(f"Merge Sort: {merge_sort(test_array)}")
print(f"Quick Sort: {quick_sort(test_array)}")
print(f"Heap Sort: {heap_sort(test_array)}")

# Test radix sort with positive integers
positive_array = [170, 45, 75, 90, 2, 802, 24, 66]
print(f"\nRadix Sort test: {positive_array}")
print(f"Radix Sort: {radix_sort(positive_array.copy())}")

# Performance comparison
def time_sort_algorithm(sort_func, arr, name):
    """Time a sorting algorithm"""
    start_time = time.time()
    sorted_arr = sort_func(arr.copy())
    end_time = time.time()
    print(f"{name}: {end_time - start_time:.6f} seconds")
    return sorted_arr

# Test with larger array
large_array = [random.randint(1, 1000) for _ in range(1000)]
print(f"\nTiming comparison with 1000 elements:")
time_sort_algorithm(bubble_sort, large_array, "Bubble Sort")
time_sort_algorithm(merge_sort, large_array, "Merge Sort")
time_sort_algorithm(quick_sort, large_array, "Quick Sort")
time_sort_algorithm(heap_sort, large_array, "Heap Sort")
```

---

## Summary of Time and Space Complexities

|Algorithm/Data Structure|Operation|Time (Best)|Time (Average)|Time (Worst)|Space|
|---|---|---|---|---|---|
|**Queue (SLL/DLL)**|Enqueue/Dequeue|O(1)|O(1)|O(1)|O(n)|
|**Stack (SLL/DLL)**|Push/Pop|O(1)|O(1)|O(1)|O(n)|
|**Circular Queue**|Enqueue/Dequeue|O(1)|O(1)|O(1)|O(n)|
|**Reverse Linked List**|Reverse|O(n)|O(n)|O(n)|O(1) iterative, O(n) recursive|
|**Merge Sorted Lists**|Merge|O(n+m)|O(n+m)|O(n+m)|O(1) iterative, O(n+m) recursive|
|**List Convergence**|Check|O(n+m)|O(n+m)|O(n+m)|O(1) optimal, O(n) hash set|
|**BST**|Insert/Search/Delete|O(log n)|O(log n)|O(n)|O(log n)|
|**Bubble Sort**|Sort|O(n)|O(n²)|O(n²)|O(1)|
|**Merge Sort**|Sort|O(n log n)|O(n log n)|O(n log n)|O(n)|
|**Quick Sort**|Sort|O(n log n)|O(n log n)|O(n²)|O(log n)|
|**Heap Sort**|Sort|O(n log n)|O(n log n)|O(n log n)|O(1)|
|**Radix Sort**|Sort|O(d×n)|O(d×n)|O(d×n)|O(n+k)|

**Key Insights:**

- **Linked Lists**: Provide O(1) insertion/deletion but O(n) search
- **Circular Queues**: Efficiently utilize space compared to linear queues
- **Tree Operations**: Depend on tree balance; AVL trees guarantee O(log n)
- **Sorting**: Choice depends on data characteristics and constraints
- **Space-Time Tradeoffs**: Hash tables use more space for faster lookups