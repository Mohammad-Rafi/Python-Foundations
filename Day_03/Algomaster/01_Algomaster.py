'''
Q. Receipt Arithmetic   ~ (easy)

Calculate a receipt for 3 notebooks at $2.50 each, 1 pen at $1.25, $4.00 shipping, and a $1.50 bundle discount applied only to the notebooks.

Compute the subtotal before shipping, the total after shipping, and the discounted average notebook price using arithmetic operators.

Expected Output:
Subtotal: $8.75
Total: $12.75
Discounted notebook average: $2.00
'''

notebook_count = 3
notebook_cost = 2.50

pen_count = 1
pen_cost = 1.25

shipping_price = 4

bundle_discount = 1.50

sub_total = notebook_cost * notebook_count + pen_cost * pen_count

total = sub_total + shipping_price

discounted_notebook_average = (notebook_cost * notebook_count - bundle_discount) / notebook_count

print(f"Subtotal: ${sub_total:.2f}")
print(f"Total: ${total:.2f}")
print(f"Discounted notebook average: ${discounted_notebook_average:.2f}")