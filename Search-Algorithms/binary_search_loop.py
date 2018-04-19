def binary_search(array,item):
    first = 0
    last = len(array)-1
    found = False

    while first <= last and not found:
        mid = (first + last)//2
        if array[mid] == item:
            found = True
        else:
            if item < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return found