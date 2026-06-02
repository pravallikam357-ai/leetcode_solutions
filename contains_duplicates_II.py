# Problem: Contains Duplicates II
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtable,Sliding window
# Language: Python

#  Problem Description:
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#  Approach:
# Traverse the array from left to right.
#For each element:
#If it was seen before, check the index difference.
#If the difference ≤ k, return True.
#Otherwise, update its latest index..

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}

        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i

        return False
