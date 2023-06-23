#merge sort
def merge_sort(list4):
    if len(list4)>1:
        mid = len(list4) // 2

        left_list = list4[:mid]
        right_list = list4[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i=k=j=0 

        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                list4[k] = left_list[i]
                i += 1
                k += 1
            else:
                list4[k] = right_list[j]
                j += 1
                k += 1
        
        while i<len(left_list):
            list4[k] = left_list[i]
            i += 1
            k += 1
        while j<len(right_list):
            list4[k] = right_list[j]
            j += 1
            k += 1

list4 = [4,1,5,6,3,0,8,1, 4]
merge_sort(list4)
print("Merge sort       = ", list4)