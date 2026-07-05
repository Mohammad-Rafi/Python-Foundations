'''
#Problem 8

Take marks (0-100). Print grade: A(>=90), B(>=80), C(>=70), D(>=60), F(<60).
'''

marks = int(input("enter your marks : "))

if 90 <= marks <= 100:
    print("A - pass")
elif 80 <= marks < 90:
    print("B - pass")
elif 70 <= marks < 80:
    print("C - pass")
elif 60 <= marks < 70:
    print("D - pass")
elif 0 <= marks < 60:
    print("F - Fail")
else:
    print("enter valid marks (0-100)")