'''
Q. Build One Line with end ~ (medium)

Print an order status for order id 1042 with status "PAID" and next step "Ship today".

Use the end parameter so the first four print() calls combine into one line as "Order #1042: PAID". Then print the next-step line normally with print() using multiple arguments.

Expected output:
Order #1042: PAID
Next step: Ship today
'''

order_id = 1042
status = "PAID"
next_step = "Ship today"

print("Order", end=" ")
print("#", end="")
print(order_id, end=": ")
print(status)
print("Next step:", next_step)