'''
Q. Rebind One Name, Mutate Another  ~ (medium)

Show the difference between rebinding a name and mutating a shared object. The names `primary` and `alias` initially point to the same list `['red', 'green']`.

First rebind `primary` to a new list using the exact expression `primary + ["blue"]`. Then mutate the original list through `alias` by assigning "yellow" to index `0`.

Expected output:

primary: ['red', 'green', 'blue']
alias: ['yellow', 'green']
same object: False
'''


primary = ['red', 'green']
alias = ['red', 'green']

primary += ['blue']
print(f"primary: {primary}")

alias[0] = "yellow"
print(f"alias: {alias}")

print(f"same object: {primary is alias}")