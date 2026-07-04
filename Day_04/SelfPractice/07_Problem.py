'''
#Problem 7

Read distance(km) and time(hours). Calculate speed. Print: 'Speed = X km/h, which is [fast/normal/slow]'.
'''

distance = int(input("enter distance in kms: "))
time = int(input("enter the time in hrs : "))

speed = distance / time

status = {speed > 100 : "Fast",
          50 <= speed <= 100: "normal",
          20 <= speed < 50 : "slow"}
about = status[True]

print(f"Speed = {speed:.2f} km/h, which is {about}")