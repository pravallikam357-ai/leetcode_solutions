# Problem: Find the Pivot index
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Prefix sum
# Language: Python

#  Problem Description:
# Given an array of integers nums, calculate the pivot index of this array.

#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

#Return the leftmost pivot index. If no such index exists, return -1.
#  Approach:
# The idea is to find an index where the sum of elements on the left equals the sum of elements on the right.

#Calculate the total sum of the array.
#Maintain a variable left to store the sum of elements to the left of the current index.
#For each index i:
#Compute the right sum as:
#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def pivotIndex(self, nums):
        total=sum(nums)
        left=0
        for i in range(len(nums)):
            right=total-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1
