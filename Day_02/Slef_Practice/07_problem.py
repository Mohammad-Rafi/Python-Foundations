'''
#Problem 7

Use sys.stdin to read 5 lines of input. Print each line prefixed with its line number.
'''

import sys

lines = [sys.stdin.readline().strip() for _ in range(5)]

for i, line in enumerate(lines, start=1):
    print(f"{i}: {line}")