'''
#Problem 4

Compare two numbers. Print which is larger, or 'equal' if same.
'''

n = int(input("enter a number : "))
m = int(input("enter a number : "))

if n > m:
    print(f"{n} is bigger number.")
    
elif n < m:
    print(f"{m} is bigger number.")
    
elif n == m:
    print(f"{n} and {m} are equal.")