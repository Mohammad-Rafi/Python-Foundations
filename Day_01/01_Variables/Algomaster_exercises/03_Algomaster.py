'''
Q. Share One Grocery List ~ (medium)

Model one grocery cart that has two names. The list `cart` already contains "apple", "bread", and "milk".

Bind `items` to the exact same list object as `cart`; do not make a copy. Then append the string "eggs" through the name `items`.

Exepcted Output:

cart: ['apple', 'bread', 'milk', 'eggs']
items: ['apple', 'bread', 'milk', 'eggs']
same object: True
'''

cart = ["apple", "bread", "milk"]
items = cart
cart.append("eggs")

print(f"cart: {cart}")
print(f"items: {items}")
print(f"same object: {cart is items}")