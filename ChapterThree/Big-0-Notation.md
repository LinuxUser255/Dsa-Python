Big O Notation
There are a lot of existing algorithms; some are fast and some are slow. Some use lots of memory. It can be hard to decide which algorithm is the best to solve a particular problem.

"Big O" analysis (pronounced "Big Oh", not "Big Zero") is one way to compare the practicality of algorithms by classifying their time complexity.

Big O is a characterization of algorithms according to their worst-case growth rates

We write Big-O notation like this:

O(formula)

Where formula describes how an algorithm's run time or space requirements grow as the input size grows.

```
O(1) - constant
O(log n) - logarithmic
O(n) - linear
O(n^2) - squared
O(2^n) - exponential
O(n!) - factorial
```

The following chart shows the growth rate of several different Big O categories. The size of the input is shown on the x axis and how long the algorithm will take to complete is shown on the y axis.

---

## Big O Notation falls under the category of culprits for Bad Performance


So, in addition to Big O, Keep in mind **Cyclomatic Complexity** too 
which measures the number of linear paths through code.

**all branching points:**
if statements, soops for and while statements increase code complexity.
