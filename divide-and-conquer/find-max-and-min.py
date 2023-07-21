"""
Let's write an algorithm to find the maximum and minimum numbers in a given array.

First, let's use the naive approach:

>>> naive([3,4,2,0,1])
(0, 4)

We have to put all tests up here so doctest will see it:

>>> max_min([3,4,2,0,1])
(0, 4)
"""
def naive(arr):
    max = min = arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] > max: max = arr[i]
        if arr[i] < min: min = arr[i]
    return (min, max)
"""
The number of comparisons in the naive approach is (2n - 2). But we can do better with the divide and conquer approach:

1. Divide the array into two halves
2. Recursively find the max and min numbers in each half
3. Combine the results by choosing the largest max and the smallest min

Base case, n = 1: that one element is both the min and max
Base case, n = 2: compare the two elements to find min and max
"""
def max_min(arr):
    l, r = 0, len(arr)-1
    return max_min_b(arr, l, r)

def max_min_b(arr, l, r):
    # where n is the size of our subproblem
    n = r - l + 1 # we add one because r is inclusive
    # base case: comparing two or less elements
    if n <= 2:
        if arr[l] <= arr[r]: return (arr[l], arr[r])
        else: return (arr[r], arr[l])
    # recursively find the max and min in each half
    mid = (l + r) // 2
    l_min, l_max = max_min_b(arr, l, mid)
    r_min, r_max = max_min_b(arr, mid+1, r)
    # pick the smallest min and the greatest max
    min = l_min if l_min < r_min else r_min
    max = l_max if l_max > r_max else r_max
    return (min, max)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
