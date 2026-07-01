'''
#Problem 9

9. Type Conversion
Read a string "123".

Convert to int and add 10.

Convert back to string and concatenate " apples".
👉 Concept: Casting between types.
'''

s = "123"
print(s, id(s), type(s))

a = int(s)
print(a, id(a), type(a))

a += 10
print(a, id(a), type(a))

b = str(a)
print(b + " apples", id(b), type(b))