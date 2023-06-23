
#find Wheather given number is power of 2 or not

def powTwo(n):
    if n == 2 or n==1:
        return True
    if n % 2 !=0 or n < 0 :
        return False
    
    return True and powTwo(n/2.0)


