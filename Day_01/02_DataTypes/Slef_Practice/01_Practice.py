'''
# Problem 1

1. String Basics
Take a string "Python".

Print its first and last character using indexing.

Try to change one character (s[0] = "J") and observe the error.
👉 Concept: Strings are immutable.
'''

s = "Python"

print(s[0])
print(s[-1])
print(s, id(s))


#correct way for mutate strings but now they are different after operating object changes and address too
s = "".join([s,"j"])
print(s, id(s))


#wrong way to mutate strings
s[0] = "j"
print(s)