def bubblesort_large(arr):
    """Returns a sorted list via O(n^2) time complexity
    Sorts in increasing order by first sorting the largest
    values
    
    arr = a list

    Improvement made allows the algorithm to stop early if
    the list has become sorted.
    """
    exchanges = True
    pass_number = len(arr)-1
    while pass_number > 0 and exchanges:
        exchanges = False
        for i in range(pass_number):
            print(arr)
            if arr[i] > arr[i+1]:
                exchanges = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        pass_number -= 1

