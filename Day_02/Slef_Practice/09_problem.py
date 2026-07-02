'''
#Problem 9

Redirect print output to a file 'output.txt' using file= parameter. Write 3 lines.
'''

#used for writing into the file created.
f = open("output.txt", "w")
print("this is line 1", file=f)
print("this is line 2", file=f)
print("this is line 3", file=f)
f.close()

#used for reading from the file whcih is written in it.
f = open("output.txt", "r")
print(f.read())
f.close()