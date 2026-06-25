# Problem: Squares of sorted array
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Two pointer,Sorting
# Language: Python

#  Problem Description:
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#  Approach:
# Create an empty list l.
#Traverse the given array:
#Take each element.
#Find its square:
#Store the square in the list.
#After creating all squared values, sort the list:
#Return the sorted squared values.
#  Time Complexity: O(n log n)
#  Space Complexity: O(n)
class Solution(object):
    def sortedSquares(self, nums):
        l=[]
        for i in range(len(nums)):
            sq=nums[i]**2
            l.append(sq)
        l.sort()
        return l
        
