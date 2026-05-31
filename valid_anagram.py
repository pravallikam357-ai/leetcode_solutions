# Problem: Valid Anagram
# Platform: LeetCode
# Difficulty: Easy
# Topic: Hashtable,strings,sorting
# Language: Python

#  Problem Description:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise
#  Approach:
#sorted(s) sorts all characters of s.
#sorted(t) sorts all characters of t.
#If the sorted character sequences are identical, the strings are anagrams; otherwise, they are not.

#  Time Complexity: O(n log n)
#  Space Complexity: O(n)
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)
