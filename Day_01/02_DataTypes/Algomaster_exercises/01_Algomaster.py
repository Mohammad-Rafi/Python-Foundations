'''
Q. Create a Product Record with Basic Types ~ (easy)

Print a product record for `Wireless Mouse` with quantity `5`, price `29.99`, in-stock flag `True`, and discount code `None`.

Store those values using the built-in types `str`, `int`, `float`, `bool`, and `NoneType`, then let the existing print calls show each value and its runtime type name.

Expected Output:

Product: Wireless Mouse (str)
Quantity: 5 (int)
Price: 29.99 (float)
In stock: True (bool)
Discount code: None (NoneType)
'''

data = {
    "Product" : "Wireless Mouse",
    "Quantity" : 5,
    "Price" : 29.99,
    "In stock" : True,
    "Discount code" : None
}

for key,value in data.items():
    print(f"{key}: {value} ({type(value).__name__})")
