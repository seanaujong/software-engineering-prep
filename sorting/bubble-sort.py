"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

This algorithm is not suitable for large data sets as its average and worst-case time complexity is O(n^2).

Unlike selection sort, bubble sort has a lower bound of O(n) if the array is already sorted.

In this algorithm, 

- Traverse from left and compare adjacent elements and the higher one is placed at right side. 
- In this way, the largest element is moved to the rightmost end at first. 
- This process is then continued to find the second largest and place it and so on until the data is sorted.
- If we did not swap any elements during a pass, we know the array is already sorted.

>>> bubble_sort([3,4,2,0,1])
[0, 1, 2, 3, 4]
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
