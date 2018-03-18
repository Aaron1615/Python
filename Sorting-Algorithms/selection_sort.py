def selection_sort(arr,loc=0):
    """Selection sort sorting algorithm with O(n^2) time complexity.
    
    Subdivides a list into two groups, sorted and unsorted.
    Searches for the minimum number and swaps it with the leftmost unsorted
    element then moves the boundaries between sorted and unsorted groups to
    the right"""
    minimum = arr[loc]
    for i in range(loc, len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]
            spot = i
    if minimum != arr[loc]:
        arr[spot] = arr[loc]
        arr[loc] = minimum
    loc += 1
    if loc >= len(arr)-1:
        return arr
    else:
        return selection_sort(arr,loc)

