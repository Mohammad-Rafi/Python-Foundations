'''
#Problem 10

Take 3 numbers. Find the largest using nested if-else (no max() function).
'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b >= c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)