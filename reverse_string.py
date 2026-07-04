# Problem: Reverse String
# Platform: LeetCode
# Difficulty: Easy
# Topic: Two pointers,String
# Language: Python

#  Problem Description:
# Write a function that reverses a string. The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.

#  Approach:
# Initialize two pointers:
#left = 0 (first character)
#right = len(s) - 1 (last character)
#While left < right:
#Swap the characters at left and right.
#Move left one step to the right (left += 1).
#Move right one step to the left (right -= 1).
#Continue until both pointers meet or cross.
#The string is reversed in-place without using extra space..

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def reverseString(self, s):

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
