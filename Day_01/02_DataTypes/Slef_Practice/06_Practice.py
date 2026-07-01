'''
# Problem 6

6. Tuple Immutability
Create t = (1, 2, 3).

Try t[0] = 99.
👉 Concept: Tuples are immutable.
'''

t = (1,2,3)
print(t, id(t), type(t))

# correct way to add values to tuple but still it is immutable the address doesnot match with initial
t = t + (5, 6)
print(t, id(t))


#wrong way to add the values to tuple
m = (1,4,6,5)
m[0] = 9
print(m)    #TypeError: 'tuple' object does not support item assignment

