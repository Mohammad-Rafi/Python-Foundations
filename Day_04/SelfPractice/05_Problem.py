'''
#Problem 5

Read two numbers. Print their average, and whether average is greater than 50 (True/False).
'''

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

avg = a + b /2

average = {
    avg > 50 : True,
    avg < 50 : False
           } 
status = average[True]
print(f"{avg}, which is {status}")