# def quick(a):
#     leng = len(a)
#     if leng <= 1 :
#         return a
    
#     pivot = a.pop()
#     greater = []
#     smaller = []
    
#     for i in a:
#         if i < pivot:
#             smaller.append(i)
#         else:
#             greater.append(i)
    
#     return quick(smaller) + [pivot] + quick(greater)


# arr = [5,3,7,4,7,1,9,0,7,8,6,5,8,4]
# print(arr)
# print(quick(arr))


def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[i+1] and arr[high] to place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


my_list = [5, 2, 4, 6, 1, 3]
quick_sort(my_list, 0, len(my_list) - 1)
print(my_list)
