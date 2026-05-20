# Problem: Perfect Number
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math
# Language: Python

#  Problem Description:
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

#Given an integer n, return true if n is a perfect number, otherwise return false.


#  Approach:
# A perfect number is a number whose proper divisors sum to the number itself.
#Start the sum with 1 because 1 is always a divisor.
#Traverse only from 2 to √num:
#If i divides num,
#then both i and num // i are divisors.
#Add both divisors to the sum.
#Avoid adding the same divisor twice for perfect squares.
#Finally:
#If sum equals num → return True
#Otherwise → return False
#  Time Complexity: O(√n)
#  Space Complexity: O(1)
import math

class Solution(object):
    def checkPerfectNumber(self, num):

        if num <= 1:
            return False

        add = 1

        for i in range(2, int(math.sqrt(num)) + 1):

            if num % i == 0:

                add += i

                if i != num // i:
                    add += num // i

        return add == num
