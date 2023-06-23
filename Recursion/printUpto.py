def number(n):
    if n == 1:
        print(n)
    else:
        number(n-1)
    print(n);
    
number(10)