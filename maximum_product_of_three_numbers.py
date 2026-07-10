# Problem: Maximum of three numbers
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Math,Sorting
# Language: Python

#  Problem Description:
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

#  Approach:
# After sorting the array, there are only two possible candidates for the maximum product:
#Product of the three largest numbers
#Product of the two smallest numbers and the largest number
#If the first two numbers are negative, their product becomes positive.
#Multiplying this positive value by the largest positive number may produce a larger product than using the three largest numbers.

#  Time Complexity: O(n log n)
#  Space Complexity: O(1)
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        n=len(nums)
        pro1=nums[n-1]*nums[n-2]*nums[n-3]
        pro2=nums[0]*nums[1]*nums[n-1]
        if pro1>pro2:
            return pro1
        else:
            return pro2
