def selection_sort(arr):
    """Selection sort sorting algorithm with O(n^2) time complexity.
    
    Subdivides a list into two groups, sorted and unsorted.
    Searches for the minimum number and swaps it with the leftmost unsorted
    element then moves the boundaries between sorted and unsorted groups to
    the right
    
    arr = a list

    """
    for number_pass in range(len(arr)-1,0,-1):
        position_of_max = number_pass
        for index in range(number_pass):
            if arr[index] > arr[position_of_max]:
                position_of_max = index
        temp = arr[number_pass]
        arr[number_pass] = arr[position_of_max]
        arr[position_of_max] = temp

arr = [5,1,1,1,13,6]
selection_sort(arr)
print(arr)
