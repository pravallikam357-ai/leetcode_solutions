# Problem: Find the index of the first occurance of the string
# Platform: LeetCode
# Difficulty: Easy
# Topic: Two pointers,String,String matching
# Language: Python

#  Problem Description:
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#  Approach:
# Find the lengths of haystack (n) and needle (m).
#If needle is longer than haystack, it cannot be present, so return -1.
#Traverse every possible starting index from 0 to n - m.
#For each starting index i:
#Compare the characters of needle with the corresponding characters in haystack.
#Continue comparing until:
#all characters match (j == m), or
#a mismatch occurs.
#If all characters match, return the starting index i.
#If no match is found after checking every position, return -1..

#  Time Complexity: O(n * m)
#  Space Complexity: O(1)
class Solution(object):
    def strStr(self, haystack, needle):
        n=len(haystack)
        m=len(needle)
        if m>n:
            return -1
        for i in range(0,n-m+1):
            j=0
            while j<m and haystack[i+j]==needle[j]:
                j=j+1
            if j==m:
                return i
        return -1
