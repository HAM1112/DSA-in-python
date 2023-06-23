
# def ascending(arr,size):
    
#     for i in range(size):
#         minval = i
#         for j in range(i+1,size):
#             if arr[j] < arr[minval]:
#                 minval = j
            
#             arr[i] , arr[minval] = arr[minval],arr[i]

# arr = [4,3,6,7,3,7,8,2,8,2,1]
# size = len(arr)

# ascending(arr,size)
# print(arr)


# def selection(a):
#     for i in range(len(a)):
#         minval = i
#         for j in range(i+1,len(a)):
#             if a[minval] > a[j] :
#                 minval = j
        
#         a[minval] , a[i] = a[i] , a[minval]
    
# arr = [2,5,3,4,7,8,5,7,0,7,5,3,9,4,8,1,23,1,2,4,2,68,5,3,8,9,0]
# print(arr)   
# selection(arr)
# print(arr)   


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

my_list = [3,56,8,9,9342,73,8,9,95,35,3,12,35,7,0,59,0,5,85,25,1,1,2,34,54,889,59575,7]
selection_sort(my_list)
print(my_list)
