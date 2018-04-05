def shell_sort(alist):
    """This function utilizes gap_insertion_sort to incrementally
    sort alist"""
    num_sublist = len(alist)//2
    while num_sublist > 0:
        
        for start in range(num_sublist):
            gap_insertion_sort(alist,start,num_sublist)
        
        num_sublist =num_sublist//2

def gap_insertion_sort(alist,start, gap):
    """Given alist, a start location, and a gap, this function
    iterates through all nodes a certain number (gap) nodes away 
    and sorts them utilizing insertion sort principals"""
    for index in range(start+gap, len(alist), gap):
        current_val = alist[index]
        position = index

        while position >=gap and alist[position-gap]>current_val:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = current_val

