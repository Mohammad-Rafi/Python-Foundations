'''
#Problem 6

Use shorthand assignment operators (+=, -=, *=, /=) in a loop. Start with x=10, apply each once.
'''

x = 10

operations = ["+=", "-=", "*=", "/="]

for i in operations:
    if i == "+=":
        x += 5
    elif i == "-=":
        x -= 5
    elif i == "*=":
        x *= 5
    elif i == "/=":
        x /= 5
    else:
        print("there is no suitable shorthand operation found.")

print("final value : ", x)