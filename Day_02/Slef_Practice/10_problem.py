'''
#Problem 10

Use eval() safely: read a math expression from input, evaluate, print result.
'''

expr = input("Enter a math expression: ")

result = eval(expr, {"__builtins__": None}, {})
print("Result:", result)
