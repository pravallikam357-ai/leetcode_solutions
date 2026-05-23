# Problem: Third Maximum Number
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Sorting
# Language: Python

# Problem Description:
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

#  Approach:
# Find the first two maximum numbers in the array and remove them and find the maximum again .

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))   # remove duplicates
        
        if len(nums) < 3:
            return max(nums)
        
        nums.remove(max(nums))
        nums.remove(max(nums))
        
        return max(nums)
