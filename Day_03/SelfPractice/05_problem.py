'''
#Problem 5

Demonstrate operator precedence: calculate 2 + 3 * 4 ** 2 / 8 - 1. Show step-by-step.
'''

result = 2 + 3 * 4 ** 2 / 8 - 1

step1 = 4 ** 2
step2 = 3 * step1
step3 = step2 / 8
step4 = step3 + 2
step5 = step4 - 1

result = step5

print(result)


# precedence order -->   () > ** > * > / > +, -