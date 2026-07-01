'''
# Problem 3

Swap two variables a = 5 and b = 10 without using a temporary variable. Print before and after.
'''

a = 5
b = 10
print(a, b)

a, b = b, a
print(a, b)
