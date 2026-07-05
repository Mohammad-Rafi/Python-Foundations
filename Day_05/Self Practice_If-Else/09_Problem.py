'''
#Problem 9

Check if a number is divisible by both 3 and 5. Print appropriate message.
'''

n = int(input("enter a number to check divisibility (3 and 5) : "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5 numebers")
elif n % 3 == 0:
    print(f"{n} only divisble by 3")
elif n % 5 == 0:
    print(f"{n} only divisble by 5")
else:
    print("not divisible by both numebrs.")