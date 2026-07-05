'''
#Problem 7

Check if a character is vowel or consonant. Handle uppercase and lowercase.
'''

charecter = input("Enter any letter : ")
k = charecter.lower()
vowels = ["a","e","i","o","u"]

if k in vowels:
    print("ovels")
elif k not in vowels:
    print("Consonant")
else:
    print("enter a valid input")
    