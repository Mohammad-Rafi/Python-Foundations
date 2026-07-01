'''
# Problem 4

Take user input for name and age. Store in variables and print: 'Hello [name], you are [age] years old.'
'''

name = input("enter name : ")
age = int(input("enter age : "))

#format() method
print("hello {}, You are {} years old".format(name, age))

#f-string
print(f"hello {name}, you are {age} years old.")

#concatination(+) and commas(,)
print("hello " + name + ", you are " + str(age) + " years old.")
print("hello", name,", you are", age,"years old.")

# formatting %
print("hello %s, you are %d years old." %(name,age))

