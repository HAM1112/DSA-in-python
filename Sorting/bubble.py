
# def bubble(arr):
#     lenght  = len(arr)
#     Sort = False
#     while not Sort:
#         Sort = True
#         for i in range(lenght-1):
#             if arr[i] > arr[i+1]:
#                 Sort = False
#                 arr[i] , arr[i+1] = arr[i+1] , arr[i]
       
# arr = [3,6,2,4,6,8,7,6,5,4,3,4]
# bubble(arr)
# print(arr)  

# def bubble(a):
#     leng = len(a)
#     sort = False
#     while not sort:
#         sort = True
#         for i in range(leng-1):
#             if a[i] > a[i+1]:
#                 sort = False
#                 a[i] , a[i+1] = a[i+1], a[i]

# arr = [3,6,4,5,7,9,6,7,5,4,3,0,1,5,8,0,4,6,1,5]
# print(arr) 
# bubble(arr)
# print(arr)

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Usage example
my_list = [5, 2, 4, 6, 1, 3]
bubble_sort(my_list)
print(my_list)
