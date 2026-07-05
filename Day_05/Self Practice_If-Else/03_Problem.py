'''
#Problem 4

Take age as input. Print 'Adult' if >= 18, else 'Minor'.
'''

age = int(input("enter your age : "))

if age >= 18:
    print("Adult")
elif 0 < age < 18:
    print("Minor")
else:
    print("Enter a valid inout")