def merge_sort(alist,front=0,back=0):
    """Takes alist as input sorting and returning the list"""
    if back == 0:
        back = len(alist)
    if (back-front) > 1:
        mid = (front+back)//2
        left_list = merge_sort(alist,front,mid)
        right_list = merge_sort(alist,mid,back)
        left_index = 0
        right_index = 0
        left_end = len(left_list)
        right_end = len(right_list)
        merged_list=[]
        while 0 < (left_end-left_index) or 0 < (right_end-right_index):
            print("in")
            if (left_end-left_index) == 0:
                merged_list.append(right_list[right_index])
                right_index += 1
            elif (right_end - right_index) == 0:
                merged_list.append(left_list[left_index])
                left_index += 1                
            else:
                if left_list[left_index] > right_list[right_index]:
                    merged_list.append(right_list[right_index])
                    right_index +=1
                else:
                    merged_list.append(left_list[left_index])
                    left_index += 1            
        return merged_list
    elif len(alist) == 0:
        return alist
    else:
        temp_list = []
        temp_list.append(alist[front])
        return temp_list
print(merge_sort([11,1,1,1,1,1,1,1,1,1,1,2,3,4,2,7,3,6,4,6,4]))