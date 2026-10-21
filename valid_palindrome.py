# Problem: Valid Palindrome
# Platform: LeetCode
# Difficulty: Easy
# Topic: Two pointers ,Strings
# Language: Python

#  Problem Description:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise

#  Approach:
# Use isalnum() and lower() functions to check whether it is alpha numeric or not and to convert to lower case

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        r=""
        for i in s:
            if i.isalnum():
                r+=i
        if r[::-1]==r:
            return True
        else:
            return False 
