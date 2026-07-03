'''
#Problem 4

Use logical operators and, or, not to check: age > 18 AND income > 50000.
'''

age = int(input("enter your age : "))
income = int(input("enter your income : "))

print(age > 18 and income > 50000)
print(age > 18 or income > 50000)
print(not(age > 18 and income > 50000))
