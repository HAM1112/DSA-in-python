# sum of array using recursion

a =[1,2,3,4,5,6,7,8]
def sumofarray(arr):
    lenght = len(arr)
    if lenght == 1:
        return arr[0]
    
    return arr[lenght-1] + sumofarray(arr[:lenght-1])


print(sumofarray([1,2,3]))