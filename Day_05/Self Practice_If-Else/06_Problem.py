'''
#Problem 6

Take temperature. Print 'Cold' if < 15, 'Warm' if 15-30, 'Hot' if > 30.
'''

temperature = float(input("enter temperature : "))

if temperature > 30:
    print("Hot")
elif 15 < temperature <= 30:
    print("Warm")
elif 0 < temperature <= 15:
    print("Cold")