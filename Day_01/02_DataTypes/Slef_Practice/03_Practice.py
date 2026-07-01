'''
#Problem 3

3. Float Precision
Create a float pi = 3.14159.

Print it with only 2 decimal places.
👉 Concept: Formatting floats.
'''

pi = 3.14159

print(round(pi, 2))

print(f"{pi:.2f}")

print("%.2f" % pi)

print("{:.2f}".format(pi))