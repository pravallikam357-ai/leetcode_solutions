# Problem: Contains Duplicates
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtable,Sorting
# Language: Python

#  Problem Description:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#  Approach:
# Convert the list nums into a set.
#A set stores only unique elements, so any duplicates are automatically removed.Compare:
#len(nums) → original number of elements
#len(set(nums)) → number of unique elements
#If the lengths are different, duplicates exist, so return True.
#Otherwise, return False.

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
