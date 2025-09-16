# Problem: Two Sum (LeetCode #1)
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)

