# Problem: Remove Trailing zeroes from a given string
# Platform: LeetCode
# Difficulty: Easy
# Topic: Strings
# Language: Python

#  Problem Description:
# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string..

#  Approach:
# Take the string as integer and obtain the last digit if zero the delete otherwise return the same integer as a string.

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def removeTrailingZeros(self, num):
        num=int(num)
        d=num%10
        while d==0:
            num=num//10
            d=num%10
        return str(num)
