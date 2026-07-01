'''
# Problem 5

5. List Mutability
Create nums = [1, 2, 3].

Change nums[0] = 99.

Print before and after.
👉 Concept: Lists are mutable.
'''

nums = [1, 2, 3]
print("before : ",nums, id(nums))


nums[0] = 99
print("after : ",nums, id(nums))

