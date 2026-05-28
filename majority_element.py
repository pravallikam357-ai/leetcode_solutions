# Problem: Majority Element
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtable,divide and conquer ,sorting,counting
# Language: Python

#  Problem Description:
# Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

#  Approach:
#First, sort the array.
#In a sorted array, the majority element (appearing more than n/2 times) will always occupy the middle position.
#So return the element at index len(nums)//2.

#  Time Complexity: O(n log n)
#  Space Complexity: O(1)
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
