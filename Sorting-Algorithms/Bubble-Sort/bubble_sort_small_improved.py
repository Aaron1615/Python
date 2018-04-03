def bubblesort_small(arr):
    """Returns a sorted list via O(n^2) time complexity.
    Sorts in increasing order by first sorting the smallest
    values
    
    arr = a list

    Improvement made allows the algorithm to stop early if
    the list has become sorted.
    """
    pass_number = 0
    exchanges = True
    while pass_number < len(arr) and exchanges:
        exchanges = False
        for i in range(len(arr)-1, pass_number, -1):
            print(arr)
            if arr[i] < arr[i-1]:
                exchanges = True
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
        pass_number += 1