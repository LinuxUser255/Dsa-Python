# Big O Notation

There are many existing algorithms; some are fast, some are slow, and some use lots of memory. It can be hard to decide which algorithm is best for solving a particular problem.

"Big O" analysis (pronounced "Big Oh", not "Big Zero") is one way to compare algorithms by classifying their **time complexity** and **space complexity**.

Big O characterizes algorithms according to their **worst-case growth rates** as input size increases.

## Notation

We write Big O notation like this:

**O(formula)**

Where `formula` describes how an algorithm's run time or space requirements grow as the input size grows.

## Common Time Complexities (from best to worst)
```
O(1)      - Constant     - Array access, hash table lookup
O(log n)  - Logarithmic  - Binary search, balanced tree operations
O(n)      - Linear       - Simple loop through array
O(n log n)- Linearithmic - Efficient sorting (merge sort, quicksort)
O(n²)     - Quadratic    - Nested loops, bubble sort
O(2ⁿ)     - Exponential  - Recursive fibonacci, subset generation
O(n!)     - Factorial    - Permutations, traveling salesman (brute force)
```

**Note:** You're missing **O(n log n)**, which is very important! It's the time complexity of efficient sorting algorithms like merge sort and quicksort.

## Growth Rate Visualization

The following chart shows the growth rate of different Big O categories:
- **X-axis:** Size of input (n)
- **Y-axis:** Time or space required

*[Your chart would go here]*

As input size grows:
- O(1) stays flat
- O(log n) grows very slowly
- O(n) grows linearly
- O(n²) grows rapidly
- O(2ⁿ) and O(n!) become impractical very quickly

## Big O vs. Cyclomatic Complexity

Big O Notation measures **algorithmic efficiency** (how performance scales with input size).

**Cyclomatic Complexity** measures **code complexity** (the number of independent paths through code).

### Cyclomatic Complexity

- Measures the number of linearly independent paths through code
- **All branching points increase complexity:**
  - `if` statements
  - `for` and `while` loops
  - `switch/case` statements
  - `&&` and `||` operators
  - Exception handlers

**Key Difference:**
- **Big O:** "How does this scale with data size?"
- **Cyclomatic Complexity:** "How difficult is this code to understand and test?"

Both are important for writing maintainable, performant code, but they measure different things.

## Example Comparisons

| Algorithm | Big O | What it means |
|-----------|-------|---------------|
| Access array by index | O(1) | Same time regardless of array size |
| Binary search sorted array | O(log n) | Doubles input size, adds one step |
| Linear search | O(n) | Doubles input size, doubles time |
| Bubble sort | O(n²) | Doubles input size, quadruples time |

---

## Tips for Analysis

- **Drop constants:** O(2n) → O(n)
- **Drop lower-order terms:** O(n² + n) → O(n²)
- **Different inputs use different variables:** O(a + b) not O(n)
- **Consider both time AND space complexity**