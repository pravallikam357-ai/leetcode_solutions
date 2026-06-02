# Problem: Find all numbers Disappered in an array
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtable
# Language: Python

#  Problem Description:
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

#  Approach:
# The array nums contains values in the range 1 to n (where n = len(nums)).
#You convert the list into a set for fast lookup.
#Then iterate from 1 → n and check:
#If a number is not in the set, it is missing → add to result list.
#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        s=set(nums)
        a=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                a.append(i)
        return a
