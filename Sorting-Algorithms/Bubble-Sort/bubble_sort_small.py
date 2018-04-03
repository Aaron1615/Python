def bubblesort_small(arr):
    """Returns a sorted list via O(n^2) time complexity.
    Sorts in increasing order by first sorting the smallest
    values
    
    arr = a list

    """
    for pass_number in range(0,len(arr)):
        for i in range(len(arr)-1, pass_number, -1):
            if arr[i] < arr[i-1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp