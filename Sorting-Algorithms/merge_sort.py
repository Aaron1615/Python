def merge_sort(alist):
    """Takes alist as input sorting and returning the list"""
    if len(alist) > 1:
        left_list = merge_sort(alist[:len(alist)//2])
        right_list = merge_sort(alist[len(alist)//2:])
        merged_list=[]
        while len(left_list) >= 1 or len(right_list) >= 1:
            if len(left_list) == 0:
                merged_list.append(right_list.pop(0))
            elif len(right_list) == 0:
                merged_list.append(left_list.pop(0))
            else:
                if left_list[0] > right_list[0]:
                    merged_list.append(right_list.pop(0))
                else:
                    merged_list.append(left_list.pop(0))
        return merged_list
    else:
        return alist