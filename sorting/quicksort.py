"""
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

To place the pivot in its sorted position, partition() will put all the smaller elements to the pivot's left, and all the larger elements to the pivot's right.

QuickSort then calls partition() recursively on each side of the pivot.

There are different choices for picking pivots:

- first element
- last element
- random element
- middle element

In this implementation, we will pick the last element as the pivot.

https://www.youtube.com/watch?v=0ko2HxqFuvk

QuickSort's partition algorithm:

- start from the leftmost element
- keep track of the index of smaller or equal elements as i.
- while traversing, if we find a smaller element, we swap the current element with arr[i]
- otherwise, ignore the current element

>>> arr = [3,4,2,0,1]
>>> quick_sort(arr)
>>> print(arr)
[0, 1, 2, 3, 4]

>>> arr2 = [6,5,8,9,3,10,15,12,16]
>>> quick_sort(arr2)
>>> print(arr2)
[3, 5, 6, 8, 9, 10, 12, 15, 16]

>>> arr3 = [6,9,1,8,2,4,7,3]
>>> quick_sort(arr3)
>>> print(arr3)
[1, 2, 3, 4, 6, 7, 8, 9]
"""
def quick_sort(arr):
    l, r = 0, len(arr)-1
    quick_sort_b(arr, l, r)

# l is the leftmost element in the partition
# r is the rightmost element in the partition (inclusive)
def quick_sort_b(arr, l, r):
    if not (l < r): return
    pivot = partition(arr, l, r)
    quick_sort_b(arr, l, pivot-1)
    quick_sort_b(arr, pivot+1, r)

def partition(arr, l, r):
    pivot = arr[r]
    lower = l
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[lower], arr[i] = arr[i], arr[lower]
            lower += 1
    arr[lower], arr[r] = arr[r], arr[lower]
    return lower

if __name__ == "__main__":
    import doctest
    doctest.testmod()
