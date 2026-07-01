'''
Q. Mutate a List and Extend a Tuple  ~ (medium)

Start with the list `['apple', 'bread', 'milk']` and the tuple `('Aisle 4', 'Shelf B')`.

Add the string `eggs` to the existing list in place. Create a new tuple that contains the original tuple values plus the string `Bin 12`, leaving the original tuple unchanged.

Exepcted Output:

Cart: ['apple', 'bread', 'milk', 'eggs']
Original location: ('Aisle 4', 'Shelf B')
Updated location: ('Aisle 4', 'Shelf B', 'Bin 12')
Cart type: list
Location type: tuple
'''

cart = ['apple', 'bread', 'milk']
location = ('Aisle 4', 'Shelf B')

cart.append('eggs')

updated_location = location + ('Bin 12',)

print(f'Cart: {cart}')
print(f'Original location: {location}')
print(f'Updated location: {updated_location}')
print(f'Cart type: {type(cart).__name__}')
print(f'Location type: {type(location).__name__}')

