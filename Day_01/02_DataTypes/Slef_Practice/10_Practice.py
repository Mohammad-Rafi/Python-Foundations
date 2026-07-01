'''
#Problem 10

10. Mixed Data Challenge
Create a list: [1, "hello", 3.5, True, (2,3), {"a":1}].

Loop through and print each element with its type using type().
👉 Concept: Python is dynamically typed.
'''

data = [1, "hello", 3.5, True, (2,3), {"a":1}]

#using loops
for i in data:
    print(i, "-->", type(data))
    
print("\n")

#without using loops
a = len(data)
print(data[0], type(data[0]))
print(data[1], type(data[1]))
print(data[2], type(data[2]))
print(data[3], type(data[3]))
print(data[4], type(data[4]))
print(data[-1], type(data[-1]))