'''
#Problem 3

Read a line of comma-separated numbers from input. Split, convert to int list, print the list.
'''

n = input("enter numbers seperated by commas : ")
k = n.split(",")
nums = []
for i in k:
    nums.append(int(i))
print(nums)

