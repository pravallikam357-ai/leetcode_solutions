# Problem: Concatenation of Array
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Simulation
# Language: Python

#  Problem Description:
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

#Specifically, ans is the concatenation of two nums arrays.

#Return the array ans..

#  Approach:
# Just use the extend function to add two arrays.

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def getConcatenation(self, nums):
        for i in range(1):
            nums.extend(nums)
        return nums
