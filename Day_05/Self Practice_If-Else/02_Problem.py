'''
#Problem 2

Check if a number is even or odd using if-else. Print result.
'''

n = int(input("Enter a number : "))

if n % 2 == 0:
    print(f"{n} is even number.")
    
elif n % 2 != 0:
    print(f"{n} is odd number.")
else:
    print("this is not a valid input")