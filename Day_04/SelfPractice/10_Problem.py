'''
#Problem 10

Read item price and quantity. Calculate total with 18% GST. Print itemized bill with formatting.
'''

item_price = int(input("enter item price : "))
item_quantity = int(input("enter item quantity : "))

sub_total = item_price * item_quantity

gst = 0.18

after_tax = sub_total * gst 

total = sub_total + after_tax
print(total)