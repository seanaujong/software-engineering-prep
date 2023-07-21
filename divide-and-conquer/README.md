# Divide and Conquer (and Combine)

What is the divide and conquer?

Divide and conquer is an algorithm design technique that:

1. **Divides** a large, complicated problem into smaller subproblems
2. **Conquers** the subproblems when they recursively divide into a base case
3. **Combines** the conquered subproblems into a final solution

Examples of divide-and-conquer algorithms include:

- Merge sort
- QuickSort
- Finding the maximum and minimum element from a given array

Divide and conquer template:

```
divide_conquer(a, i, j):
    if base_case(a, i, j):
        return Solution(a, i, j)
    else:
        mid = divide(a, i, j)               // f1(n) as f(n)
        b = divide_conquer(a, i, mid)       // T(n/2)
        c = divide_conquer(a, mid+1, j)     // T(n/2)
    return combine(b, c)                    // f2(n) as f(n)
```

The recurrence relation is:

```
T(n) = aT(n/b) + f(n), n > base_case
     = O(1), n = base_case

T(n) =  2T(n/2) + f(n)

where:

a = the number of subproblems created in each recursion
    BASICALLY the number of times a recursive function calls itself per recursion
  = 2 (in the template, divide_conquer calls itself twice)

n/b = the denominator for the fraction we send into
    = 2 (in the template, divide_conquer )

f(n) = cost of work outside the recursive call,
       for divide and conquer the cost of work is:
       the number of steps to divide the problem plus
       the number of steps to combine the results into a solution
```
