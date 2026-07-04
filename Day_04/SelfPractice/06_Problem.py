'''
#Problem 6

Calculate BMI from weight(kg) and height(m) input. Formula: BMI = weight / height^2. Print category.
'''

weight = float(input("enter your weight (kg): "))
height = float(input("enter your height (m): "))

BMI = weight / height ** 2

category = {
    BMI > 100 : "Obase",
    50 <= BMI <= 100 : "normal",
    0 <= BMI <= 50 : "skinny",
}

status = category[True]

print(f"{BMI}, which is {status}")