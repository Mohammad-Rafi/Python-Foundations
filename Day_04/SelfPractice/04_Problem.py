'''
#Problem 4

Take a 3-digit number as input. Extract and print each digit (hundreds, tens, ones) separately.
'''

num = input("Enter a 3-digit number: ")

hundreds = int(num[0]) * 100
tens = int(num[1]) * 10
units = int(num[2]) * 1

print("Hundreds =", hundreds)
print("Tens =", tens)
print("Units =", units)
