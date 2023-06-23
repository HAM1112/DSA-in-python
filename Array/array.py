import math

def median(arr1,arr2):
    arr3 = arr1 + arr2
    arr3.sort()
    lenght = len(arr3)
    if lenght % 2 ==0:
        median = (arr3[(lenght//2-1)] + arr3[lenght//2])/2
        return median
    else:
        median = arr3[lenght//2]
        return median/1
    
a1 = [1,3]
a2 = [2,4]

median(a1,a2)

