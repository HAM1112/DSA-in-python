
def maxArea(height):
    volume = 0
    arrlen = len(height)
    for i in range(arrlen):
        for j in range(i+1,arrlen):
            lenght = j-i
            breadth = height[min(i,j)]
            print(f"lenght {lenght} and breadth {breadth}")
            if (lenght * breadth) > volume:
                volume = lenght * breadth
    
    return volume
    
a = [1,8,6,2,5,4,8,3,7]
b = [1,1]

print(maxArea(a))