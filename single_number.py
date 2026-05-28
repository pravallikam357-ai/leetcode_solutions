# Problem: Single Number
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Bit Manipulation
# Language: Python

#  Problem Description:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space..

#  Approach:
# Access each element and count the no.of occurences and return the number which has count 1
#  Time Complexity: O(n²)
#  Space Complexity: O(1)
class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
           count=nums.count(i)
           if count==1:
               return i 
