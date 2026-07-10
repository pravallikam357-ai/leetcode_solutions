# Problem: Sqrt(x)
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math,Binary search
# Language: Python

#  Problem Description:
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

#You must not use any built-in exponent function or operator.

#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

#  Approach:
#The problem is to find the integer square root of x, i.e., the largest integer k such that:    
#Instead of checking every number from 1 to x, the solution uses Binary Search because the square values increase in sorted order
#While left <= right:

#Find the middle element:
#If no exact square root is found, right will be the largest integer whose square is less than or equal to x.

#  Time Complexity: O(log n)
#  Space Complexity: O(1)
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
