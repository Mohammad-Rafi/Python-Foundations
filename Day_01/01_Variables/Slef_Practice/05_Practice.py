'''
# Problem 5

Declare a constant PI = 3.14159. Try to 'change' it by reassigning. Document what happens.
'''

pi = 3.14159
print(pi, id(pi))

pi = pi + 1
print(pi, id(pi))

#integers are immutable because when operated they store in new objects, so new address