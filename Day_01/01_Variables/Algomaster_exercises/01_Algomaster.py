'''
Q. Bind and Rebind a Price  ~ (easy)

Track the price of the item "desk lamp". Bind `item_name` to "desk lamp" and `price` to `19.99` before the first print, then rebind only `price` to `24.99` before the final print.

The print calls are already in place; use the exact string and float literals above.

Expected Output

desk lamp: $19.99
desk lamp: $24.99
'''

item_name = "desk lamp"
price = 19.99
print(f"{item_name}: ${price:.2f}")


price = 24.99
print(f"{item_name}: ${price:.2f}")

