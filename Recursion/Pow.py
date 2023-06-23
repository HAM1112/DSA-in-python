def myPow(x,n):
    if n == 0:return 1 
    if n == 1:return x
    if n == -1: return 1/x 

    if n>0:
        return x * myPow(x,n-1)
    else:
        return (1/x) * myPow(x,n+1)


print(myPow(0.00001,2147483647))