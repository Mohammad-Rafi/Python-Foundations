'''
#Problem 7

7. Dictionary Operations
Create student = {"name": "Adam", "age": 15}.

Add a new key "cgpa": 8.9.

Delete "age".
👉 Concept: Dicts are mutable.
'''

student = {
    "name" : "Adam",
    "age" : 15
}

print(student, id(student), type(student))

student["cgpa"] = 8.9
print(student, id(student), type(student))

