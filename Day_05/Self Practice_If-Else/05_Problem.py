'''
#Problem 5

Check if a year is a leap year. (Divisible by 4, not by 100 unless by 400).
'''

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")