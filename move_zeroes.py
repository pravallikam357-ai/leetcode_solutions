# Problem: Move Zeroes
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Two pointers
# Language: Python

#  Problem Description:
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#  Approach:
# Create two arrays for zeroes and nonzeroes and merge them to move all zeroes to the end.

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def moveZeroes(self, nums):
        z = []
        nz = []

        for i in range(len(nums)):
            if nums[i] == 0:
                z.append(nums[i])
            else:
                nz.append(nums[i])

        nz.extend(z)

        for i in range(len(nums)):
            nums[i] = nz[i]
