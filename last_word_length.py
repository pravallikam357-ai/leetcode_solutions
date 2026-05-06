# Problem: Length of the last word in a given string
# Platform: LeetCode
# Difficulty: Easy
# Topic: Strings
# Language: Python

#  Problem Description:
# Find the length of the last word in the given string.

#  Approach:
# Use split method and split with spaces and find the length of last string.

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        splits=s.split()
        return len(splits[-1])
        
