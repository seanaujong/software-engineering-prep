"""
Merge sort is a recursive algorithm that continuously splits the array in half until it cannot be further divided i.e., the array has only one element left. An array with one element is always sorted. Then the sorted subarrays are merged into one sorted array.

1. Divide the array into two halves
2. Recursively sort each half
3. Combine the results by merging the two sorted lists

Base case: an array is sorted if there are 0 or 1 elements in it

>>> merge_sort([3,4,2,0,1])
[0, 1, 2, 3, 4]
"""
def merge_sort(arr):
    n = len(arr)
    # base case: arr is sorted if there are 0 or 1 elements in it
    if n <= 1: return arr
    half = n // 2
    # l_arr and r_arr are sorted
    l_arr, r_arr = merge_sort(arr[:half]), merge_sort(arr[half:])
    return merge(l_arr, r_arr)
    
# given two sorted lists l_arr and r_arr, return a combined sorted list
def merge(l_arr, r_arr):
    result = []
    while l_arr and r_arr:
        if l_arr[0] <= r_arr[0]: result.append(l_arr.pop(0))
        else: result.append(r_arr.pop(0))
    result += l_arr + r_arr
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
