def bubblesort_large(arr):
    """Returns a sorted list via O(n^2) time complexity
    Sorts in increasing order by first sorting the largest
     values
     
     arr = a list

     """
    for pass_number in range(len(arr)-1, 0, -1):
        for i in range(pass_number):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp