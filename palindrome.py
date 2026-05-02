# Problem: Palindrome
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math
# Language: Python

#  Problem Description:
# To find the given integer is palindrome or not

#  Approach:
# Converting the number into string and reverse it and compare.

# ⚡ Time Complexity: O(n)
# ⚡ Space Complexity: O(n)import math
class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        rev=y[::-1]
        if rev==y:
             return True
        else:
            return False
