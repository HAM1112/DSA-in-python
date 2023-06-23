# def quick(a):
#     leng = len(a)
#     if leng <= 1 :
#         return a
    
#     pivot = a.pop()
#     greater = []
#     smaller = []
    
#     for i in a:
#         if i > pivot:
#             greater.append(i)
            
#         else:
#             smaller.append(i)
    
#     return quick(smaller) + [pivot] + quick(greater)


# arr = [2,8,5,6,9,5,0,3,4,6,8,3,7,6,3,9,4,3,7,9]
# print(arr)
# print(quick(arr))


def quick(a):
    leng = len(a)
    if leng <=1 :
        return a
    pivot = a.pop()
    great = []
    less = []
    
    for i in a:
        if i < pivot :
            less.append(i)
        else:
            great.append(i)
    
    return quick(less) + [pivot] + quick(great)

arr = [4,5,6,3,4,3,67,8,0,1,2,5,3,2,3,0,9,0,7,3,2,1,3,5,7,0,8,5]
print(arr)
print(quick(arr))


