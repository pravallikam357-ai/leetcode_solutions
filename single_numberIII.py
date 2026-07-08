# Problem: Single NumberIII
# Platform: LeetCode
# Difficulty: Medium
# Topic: Arrays,Bit Manipulation
# Language: Python

#  Problem Description:
# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

#You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
#  Approach:
# Create an empty list a.
#Traverse each element i in nums.
#Count how many times i appears using nums.count(i).
#If the count is 1, append it to a.
#Return a.

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def singleNumber(self, nums):
        a=[]
        for i in nums:
            if nums.count(i)==1:
                a.append(i)
        return a
