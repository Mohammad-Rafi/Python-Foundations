'''
Q. Unpack Contact Details and Swap Counts ~ (medium)

Create a shipping contact by using one tuple-unpacking assignment to bind `recipient` to "Mina Patel", `city` to "Denver", and `package_count` to `3`.

The route counts start as `morning_count = 7` and `evening_count = 11`. After the first route print, swap those two names with one multiple-assignment statement.

Expected Output:

Contact: Mina Patel in Denver
Packages: 3
Before swap: morning=7, evening=11
After swap: morning=11, evening=7
'''

recipient = "Mina Patel"
city = "Denver"
package_count = 3

morning_count = 7
evening_count = 11
print("Contact: {} in {}".format(recipient, city))  
print("Packages: %d" %package_count)
print(f"Before swap: morning={morning_count}, evening={evening_count}")

#after swapping
morning_count, evening_count = evening_count, morning_count
print(f"After swap: morning={morning_count}, evening={evening_count}")
