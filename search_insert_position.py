# Problem: Search insert position
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Binarysearch
# Language: Python

#  Problem Description:
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.
# Approach:
# The array is already sorted.

#Traverse the array from left to right.
#For each element, check if it is greater than or equal to the target.
#If found, return its index because:
#If the target exists, this is its position.
#If the target does not exist, this is where it should be inserted.
#If no element is greater than or equal to the target, the target should be inserted at the end of the array, so return len(nums)

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
