'''
#Problem 5

Read multi-line input until empty line. Store all lines in a list. Print line count and all lines.
'''

line_count = list(iter(input, ""))

print(len(line_count))
print(*line_count, sep="\n")
