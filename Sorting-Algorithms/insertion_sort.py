def insertion_sort(arr):
    """Implementation of the Insertion sort algorithm with O(n^2) time complexity.
    Iterates through each index in the list placing each value at the left in the 
    proper location among previously sorted values.
    """
    for index in range(len(arr)):

        current_value = arr[index]
        position = index
        
        while position > 0 and arr[position - 1] > current_value: 

            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = current_value


