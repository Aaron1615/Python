def quick_sort(alist):
    """Sorts a given list using a divide and conquer strategy."""
    quick_sort_helper(alist,0,len(alist)-1)

def quick_sort_helper(alist,start,end):
    """Helper function used to iteratively split alist
    based on results from partition"""
    if start<end:
        pivot = partition(alist,start,end)
        quick_sort_helper(alist,start,pivot-1)
        quick_sort_helper(alist,pivot+1,end)

def partition(alist,start,end):
    """Used to partially sort alist while searching for the
    pivot value"""
    part_value = alist[start]
    left_index = start + 1
    right_index = end

    while left_index <= right_index:
        if alist[left_index] <= part_value:
            left_index += 1
        else:
            if alist[right_index] >= part_value:
                right_index -= 1
            else:
                temp = alist[left_index]
                alist[left_index] = alist[right_index]
                alist[right_index] = temp
    temp = alist[right_index]
    alist[right_index] =alist[start]
    alist[start] = temp
    return right_index