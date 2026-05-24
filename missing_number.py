# Problem: Missing Number
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hash Table,Math,Sorting,Bit Manipulation,Binary search
# Language: Python

#  Problem Description:
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

#  Approach:
# Acces each item of the array upto the given length and return the missing value between the range.

#  Time Complexity: O(n²)
#  Space Complexity: O(1)
class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        
