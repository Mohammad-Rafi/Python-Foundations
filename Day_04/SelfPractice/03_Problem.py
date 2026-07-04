'''
#Problem 3

Read principal, rate, time. Calculate simple interest. Print: 'SI = [amount] for [P] at [R]% for [T] years'.
'''

p = int(input("enter principal amount : "))
r = int(input("enter rate of interest : "))
t = int(input("enter time in years : "))

si = (p * t * r) / 100

print(si)