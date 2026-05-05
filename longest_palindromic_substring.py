# Problem: Longest palindromic substring
# Platform: LeetCode
# Difficulty: Medium
# Topic: Two pointers,strings,dynamic programming
# Language: Python

#  Problem Description:
# Find the longest palindromic substring in a given string.

# Approach:
# Obtain all substrings and check whether palindrome or not and return substring.

#  Time Complexity: O(n³)
#  Space Complexity: O(n)
class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                
                if sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub
        
        return longest
