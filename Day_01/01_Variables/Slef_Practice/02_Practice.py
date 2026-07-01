'''
# Problem 2

Create variables of types: int, float, str, bool, list, tuple, dict, set. Print each type using type().

'''

score = 10
percentage = 99.9
name = "Adam"
is_student = True
subjects = ["maths", "english", "science", "Telugu"]    #mutable
marks = (90, 85, 75, 100)   #immutable
academic_data = {   
    "name" : "Adam",
    "age" : 15,
    "cgpa" : 8.9,
    "is_passed" : True
}   #mutable
parent_details = {"Alex", "alex@mail.com", 9876543210}


print(score, type(score))
print(percentage, type(percentage))
print(name, type(name))
print(is_student, type(is_student))
print(subjects, type(subjects))
print(marks, type(marks))
print(academic_data, type(academic_data))
print(parent_details, type(parent_details))