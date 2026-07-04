'''
#Problem 9

Swap two numbers using XOR (without temp). a=5, b=7. Verify: a^=b; b^=a; a^=b. Print both.
'''

a = 5
b = 7

a ^= b
b ^= a
a ^= b
print("a =", a)
print("b =", b)