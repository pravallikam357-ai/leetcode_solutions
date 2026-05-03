# Problem: Number of Good pairs
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtables,Math
# Language: Python

#  Problem Description:
# Take the two lists and compare every two values if equal increment the count by one.

#  Approach:
# You use two nested loops:

#Outer loop picks each element i
#Inner loop checks all elements after it (j = i+1)

#  Time Complexity: O(n²)
#  Space Complexity: O(1)
class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count=count+1
        return count
        
