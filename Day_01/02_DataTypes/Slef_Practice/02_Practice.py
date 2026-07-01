'''
#Problem 2

2. Integer Mutability Test
Assign x = 5.

Print id(x).

Do x += 1 and print id(x) again.
👉 Concept: Integers are immutable; reassignment creates a new object.
'''

x = 5
print(id(x))

x += 1
print(id(x))