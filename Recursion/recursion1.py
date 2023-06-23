# fibonacci number in nth position:
def fib1(n):
    if n ==1 :
        return 0;
    elif n==2 :
        return 1 
    else :
        return fib1(n-1) + fib1(n-2)

#print(fib1(6))
    
# sum of number upto n 

def sums(n):
    if n==1 :
        return 1 ;
    return n + sums(n-1);

#print(sums(10))


#exponential using recursion 

def poww(n,x):
    if x == 0:
        return 1
    else:
        return n * (poww(n , x-1))

#print(poww(2,4))
 
#factorial 

def fact(n):
    if n == 1:
        return 1 
    else :
        return n * fact(n-1)

#print(fact(10))        

def sumArray(arr):
    pass


