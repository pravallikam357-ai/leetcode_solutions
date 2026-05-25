# Problem: Sort Colors
# Platform: LeetCode
# Difficulty: Medium
# Topic: Arrays,Two pointers,sorting
# Language: Python

#  Problem Description:
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function..

#  Approach:
# Just sort the given array.

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def sortColors(self, nums):
        nums.sort()
        return nums
