'''
# Problem 8

Use identity operators is and is not. Compare two lists with same values vs same object.
'''

list1 = [1,2,3]
list2 = [1,2,3]

#list is mutable so it creates new object even after creating same values with different variable names, each points to different object --> new memory address
print("list 1 == list 2 :", list1 == list2, id(list1))
print("list 1 is list 2 :", list1 is list2, id(list2))

list3 = list1
print("list 3 == list 1 :", list3 == list1)
print("list 3 is list 1 :", list3 is list1)
print("list 3 is not list 1 :", list3 is not list1)

print(f"same for list 1 and 3 : {id(list1)}, {id(list3)} \ndifferent for list 2 : {id(list2)}")