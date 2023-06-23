# def insertion(a):
#     lenght = len(a)
#     for i in range(1,lenght):
#         val = a[i]
#         while a[i-1] > val and i>0:
#             a[i] , a[i-1] = a[i-1] , a[i]
#             i = i-1
            
            
            
# arr = [3,5,7,9,5,7,3,5,3,4,7,3,7,9,0,1,2,4,6]
# print(arr)
# insertion(arr)
# print(arr)

# def insertion(a):
#     leng = len(a)
    
#     for i in range(1,leng):
#         check = a[i]
        
#         while check < a[i-1] and i > 0:
#              a[i] , a[i-1] = a[i-1] , a[i]
             
#              i -= 1
             
             
# arr = [ 2,4,6,8,5,6,4,66,0,8,1,4,7,5,9,0,2,4]
# print(arr)
# insertion(arr)
# print(arr)
    
def insertion_sort(arr):
# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted at the right position

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert the key at its correct position

# Usage example
my_list = [5, 2, 4, 6, 1, 3]
insertion_sort(my_list)
print(my_list)
