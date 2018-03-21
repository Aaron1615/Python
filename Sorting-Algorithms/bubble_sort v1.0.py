def bubble_sort(arr):
    """Returns a sorted list via O(n^2) time complexity."""
    sorted_arr = arr[:]
    num_changes = 0
    for i in range(1,len(arr)):
        if sorted_arr[i-1] > sorted_arr[i]:
            sorted_arr[i-1], sorted_arr[i] = sorted_arr[i], sorted_arr[i-1]
            num_changes +=1
    if num_changes > 0:
        return bubble_sort(sorted_arr)
    else:
        return sorted_arr