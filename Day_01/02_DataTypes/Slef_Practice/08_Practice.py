'''
# Problem 8

Create s = {1, 2, 2, 3}.

Print the set.
👉 Concept: Sets remove duplicates automatically.
'''

s = {1,2,2,3}
print(s,id(s))

#To add items to set use update((values))
s.update((4,4,5,6,7,7))
print(s,id(s))

