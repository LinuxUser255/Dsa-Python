# Lambda Functions

**AKA: Anonymous functions**

**Lambda functions are called "anonymous functions" because they have no name.**

Unlike trad functions that you define: `def main():`

A lambda is simply declared using the word `lambda:`

With `lambda`, you drop the `def`,  assign the name `lambda`,  drop the `()`
parenthesis, and leave the `:` colon.

So, something like `def my_func():` becomes `lambda:`


<br>

In Python (and many other languages), regular functions are defined with a name using the `def` keyword:

This function has a clear name: `square`. You can refer to it later by that name.

```python
def square(num):
    return num ** 2
```


<br>

A lambda function, however, is created without ever giving it a name:

```python
lambda num: num ** 2
```

<br>

It exists only as an expression and is "anonymous" — it has no identifier attached to it unless you explicitly assign it to a variable:

```python
# Even if you assign it, the lambda itself is still anonymous
square = lambda num: num ** 2
```

<br>

The lambda expression doesn't have its own name; it's just a temporary, nameless function object. That's why they're called **anonymous functions** — they're defined and used without being bound to a named identifier.

<br>

This makes them especially useful for short, one-off operations (e.g., as arguments to `map()`, `filter()`, `sorted()`, etc.) where creating a full named function would be unnecessarily verbose.

<br>

### In summary:  

**No name → anonymous**  
That's the whole reason for the term


### Lambda Function to Calculate the Factorial of a Number

<br>

#### Simple Example
```python
lambda num: num ** 2
```

<br>
A lambda function has three parts:

| Part 1      | Part 2          | Part 3       |
|-------------|-----------------|--------------|
| `lambda` keyword | Parameter(s)    | Expression   |

<br>

#### Key Characteristics
1. **Multiple parameters** – Parameters can be separated by commas:  
   ```python
   lambda x, y: x + y
   ```

2. **Single line** – The entire function is written on one line.

3. **No `return` statement** – The expression's value is automatically returned.

<br>

#### Example: Square a Number
```python
square = lambda num: num ** 2
print(square(5))  # Output: 25
```

<br>

#### Example: Factorial (Recursive Lambda)
```python
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))  # Output: 120
```

<br>

Lambda functions are concise and ideal for short, simple operations passed as arguments (e.g., to `map()`, `filter()`, or `sorted()`).

<br>

### Converting a Regular Function to a Lambda Function

Here’s a clean step-by-step demonstration of converting a standard function to an equivalent lambda function.

<br>

#### 1. Original Regular Function

This defines a function named `square_n` that takes one parameter (`num`) and returns its square.
```python
def square_n(num):
    return num ** 2
```

<br>


#### 2. Equivalent Lambda Function

This anonymous lambda function does exactly the same thing: it takes `num` and returns `num ** 2`.
```python
lambda num: num ** 2
```


<br>

#### 3. Step-by-Step Conversion Process

Start with the regular function:
```python
def square_n(num):
    return num ** 2
```

<br>

**Step 1:** Replace `return` with the lambda syntax 

(use the expression directly after `:`):
```python
def square_n(num):
    lambda num: num ** 2   # Incorrect – lambda can't be inside def like this
```


<br>

**Step 2** – Remove the `def`, function name, and `return` keyword entirely. The lambda stands alone:
```python
lambda num: num ** 2
```

<br>

The lambda has three parts:
- `lambda` keyword
- Parameter(s): `num`
- Expression: `num ** 2` (the result is automatically returned)

<br>

#### 4. Usage Comparison

**Regular function:**
```python
print(square_n(5))  # Output: 25
```

<br>

**Lambda function (assigned to a variable for easy calling):**
```python
square = lambda num: num ** 2
print(square(5))  # Output: 25
```

<br>

Or use it directly (common when passing to higher-order functions):
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda num: num ** 2, numbers))
# Result: [1, 4, 9, 16]
```
---

Lambda functions are ideal for short, simple operations where defining a full function feels overly verbose.

<br>