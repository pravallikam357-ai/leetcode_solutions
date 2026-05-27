# Problem: Running Sum of 1D Array
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Prefix Sum
# Language: Python

#  Problem Description:
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums..

#  Approach:
#Access each element and add every element with the next one and return the final sum
#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def runningSum(self, nums):
        run=0
        l=[]
        for i in range(len(nums)):
            run=run+nums[i]
            l.append(run)
        return l
        
