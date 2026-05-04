# Problem: Factorial Trailing zeros
# Platform: LeetCode
# Difficulty: Medium
# Topic: Math
# Language: Python

#  Problem Description:
# Find the number of trailing zeros in a factorial.

#  Approach:
# Find the number of 5's in factrs of the given number.

#  Time Complexity: O(logn)
#  Space Complexity: O(1)
class Solution(object):
    def trailingZeroes(self, n):
        count=0
        while n>0:
           n=n//5
           count+=n
        return count
