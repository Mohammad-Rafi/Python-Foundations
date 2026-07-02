'''
Q. Control Separators Between Printed Values   ~ (medium) 

Print the product names "Mouse", "Keyboard", and "Monitor" four different ways using print() and its sep parameter.

The four formats are: default spaces between names, comma-space between names, space-pipe-space between names, and one product per line using the separator string "\n".

Expected output:
Mouse Keyboard Monitor
Mouse, Keyboard, Monitor
Mouse | Keyboard | Monitor
Mouse
Keyboard
Monitor
'''

product_a = "Mouse"
product_b = "Keyboard"
product_c = "Monitor"

print(f"{product_a} {product_b} {product_c}")
print(product_a,product_b,product_c, sep=", ")
print(product_a,product_b,product_c, sep=", ")
print(product_a,product_b,product_c, sep=" | ")
print(product_a,product_b,product_c, sep="\n")
