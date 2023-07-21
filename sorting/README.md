# Sorting Observations

Based on the [CS50 - Algorithms](https://cs50.harvard.edu/x/2023/weeks/3/) lecture which covers merge sort, bubble sort, and selection sort.

## References

- [CS50 - Algorithms](https://cs50.harvard.edu/x/2023/weeks/3/)
- [GFG - Merge Sort](https://www.geeksforgeeks.org/merge-sort/)
- [GFG - Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)
- [GFG - Selection Sort](https://www.geeksforgeeks.org/selection-sort/)

## Ranking the sorting algorithms by time complexity

1. Merge sort
2. Bubble sort
3. Selection sort

Merge sort's worst and best case time complexity is O(n log n).

Bubble sort's worst case time complexity is O(n^2) but its best case time complexity is O(n). This is because the algorithm will stop if the array is already sorted (when it makes no swaps in one pass).

Selection sort's worst and best case time complexity is O(n^2). This is because the algorithm will take the same amount of operations even if the array is already sorted.

## In-place merge sort

[StackOverflow](https://stackoverflow.com/questions/2571049/how-to-sort-in-place-using-the-merge-sort-algorithm)

Merge sort is one of the fastest sorting algorithms, but it uses an extra buffer array. It's possible to implement an in-place version, but it's not easy. Don't bring the in-place version up during an interview.

## The sorted and unsorted sections of bubble sort and selection sort

Bubble sort "bubbles up" larger numbers to the right side of the unsorted array: [ unsorted | sorted ]

Selection sort swaps the smallest number into the left side of the unsorted array: [ sorted | unsorted ]

# Divide and Conquer

Let's use what we learned about sorting from CS50 to transition to an adjacent topic, divide and conquer. Merge sort and quicksort are examples of divide and conquer algorithms.
