def powThree(n):
    if n == 3 or n == 1:
        return True
    if n%3 != 0 or n <=0:
        return False
    return True and powThree(n/3)