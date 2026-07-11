'''
Q. Print a Simple Store Greeting    ~ (easy)

Print a two-line greeting for the store "MyShop", the customer "Riley", and an item count of 3.

Use the existing variables in the template. The first line should be built with an f-string, and the second line should use print() with multiple arguments so Python inserts the space after the colon.

Expected output:
Welcome to MyShop, Riley!
Items in cart: 3
'''

store_name = "MyShop"
customer_name = "Riley"
item_count = 3

print(f"Welcome to {store_name}, {customer_name}", end="!\n")
print("Items in cart:",item_count)