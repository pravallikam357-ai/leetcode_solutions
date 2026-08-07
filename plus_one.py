# Problem: Plus one
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Math
# Language: Python

#  Problem Description:
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

#  Approach:
# Start from the last digit.
#If the digit is less than 9:
#Add 1.
#Return the array.
#If the digit is 9:
#Change it to 0.
#Carry 1 to the previous digit.
#Continue from right to left.
#If every digit was 9, add 1 at the beginning.
#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        digits.insert(0,1)
        return digits


        
