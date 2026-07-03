'''
#Problem 10

Calculate compound interest: P=1000, R=5%, T=3 years. Formula: A = P*(1+R/100)**T
'''

P = 1000
R = 5
T = 3

Amount = P * (1+R/100)**T

print(f"compund interest is : ₹{Amount:.2f}")