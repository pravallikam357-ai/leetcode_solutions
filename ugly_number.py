# Problem: Ugly Number
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math
# Language: Python

# Problem Description:
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

#Given an integer n, return true if n is an ugly number..

#  Approach:
# An ugly number is a number whose only prime factors are 2, 3, and 5.

#Your logic:

#Keep dividing n by 2, 3, or 5 whenever possible
#If at some point it’s not divisible by any of them - not ugly
#If you reduce it to 1 - ugly number
#  Time Complexity: O(log n)
#  Space Complexity: O(1)
class Solution(object):
    def isUgly(self, n):
        while n>1:
            if n%2==0:
                n=n//2
            elif n%3==0:
                n=n//3
            elif n%5==0:
                n=n//5
            else:
                return False
        if n<=0:
            return False
        return True
        
