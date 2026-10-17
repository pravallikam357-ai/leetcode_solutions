# Problem: Add Binary
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math,String,Bit manipulation,Simulation
# Language: Python

#  Problem Description:
# Given two binary strings a and b, return their sum as a binary string.

#  Approach:
# 1. Initialize two pointers, i and j, at the last indices of strings a and b.
# Initialize carry = 0 and an empty result string r.
# Use a while loop while i >= 0 or j >= 0 or carry > 0.
# Get the digits at i and j. If either pointer is out of bounds, use 0.
# Calculate the sum:
#total = a_digit + b_digit + carry
# Calculate the current binary digit using total % 2.
# Update the carry using total // 2.
#Add the current digit to the beginning of the result.
#Decrease both pointers.
# Return the result string.

#  Time Complexity: O(max(n,m))
#  Space Complexity: O(max(n,m))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        r = ""

        while i >= 0 or j >= 0 or c > 0:
            a_d = int(a[i]) if i >= 0 else 0
            b_d = int(b[j]) if j >= 0 else 0

            t = a_d + b_d + c
            d = t % 2
            c = t // 2

            r = str(d) + r

            j -= 1
            i -= 1

        return r
