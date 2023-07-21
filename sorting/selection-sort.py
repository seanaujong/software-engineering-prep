"""
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 

>>> selection_sort([3,4,2,0,1])
[0, 1, 2, 3, 4]
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest = arr[i]
        smallest_i = i
        for j in range(i, n):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_i = j
        arr[i], arr[smallest_i] = arr[smallest_i], arr[i]
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
