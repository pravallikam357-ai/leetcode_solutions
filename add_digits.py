# Problem: Add Digits
# Platform: LeetCode

# Difficulty: Easy
# Topic: Math,Simulation,Number Theory
# Language: Python

#  Problem Description:
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#  Approach:
# While the number has two or more digits (num >= 10):
#Initialize tot = 0.
#Extract each digit using num % 10.
#Add the digit to tot.
#Remove the last digit using num //= 10.
#Replace num with tot.
#Repeat until num is a single digit.
#Return num.
#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def addDigits(self, num):
        while num>=10:
            tot=0
            while num>0:
                l=num%10
                tot+=l
                num=num//10
            num=tot
        return num
        
