# Problem: Count Segments
# Platform: LeetCode
# Difficulty: Easy
# Topic: Strings
# Language: Python

#  Problem Description:
# Given a string s, return the number of segments in the string.

#A segment is defined to be a contiguous sequence of non-space characters.

 
#  Approach:
# Just use the split function and find the length 

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution:
    def countSegments(self, s: str) -> int:
        str=s.split()
        return len(str)
