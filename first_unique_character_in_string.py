# Problem: First Unique character in a string
# Platform: LeetCode
# Difficulty: Easy
# Topic: Strings,queue,Hashtable,counting
# Language: Python

#  Problem Description:
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#  Approach:
# Traverse the string and store the count of every character in d.
#Traverse the string again using indices.
#The first character whose frequency is 1 is the first non-repeating character, so return its index.
#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def firstUniqChar(self, s):
        d = {}

        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1
