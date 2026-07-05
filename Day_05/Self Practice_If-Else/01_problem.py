'''
#Problem 1

Take a number. Print 'positive' if > 0, 'negative' if < 0, else 'zero'.
'''

n = int(input("Enter a number : "))

if n > 0:
    print(f"{n} is Positive number")
elif n < 0:
    print(f"{n} is Negative number")