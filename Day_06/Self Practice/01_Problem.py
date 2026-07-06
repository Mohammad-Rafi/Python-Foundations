'''
#Problem 1

Check if 3 sides form a valid triangle. If yes, check if equilateral, isosceles, or scalene.
'''

a, b, c = 3, 4, 5  

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")