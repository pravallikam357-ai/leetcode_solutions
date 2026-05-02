# Problem: Two Sum
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays
# Language: Python

#  Problem Description:
# Find two numbers that add up to a target.

#  Approach:
# Use hashmap to store values and check complement.

# ⚡ Time Complexity: O(n)
# ⚡ Space Complexity: O(n)class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
    
