# Problem: Concatenate non-zero digits and multiply by sum I
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math
# Language: Python

#  Problem Description:
# You are given an integer n.
#Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.
#Let sum be the sum of digits in x.
#Return an integer representing the value of x * sum.
#  Approach:
# Convert the number to a string.

#Build a new string x containing only non-zero digits.
#Calculate tot, the sum of those non-zero digits.
#If all digits were zero, return 0.
#Otherwise return int(x) * tot

#  Time Complexity: O(log n)
#  Space Complexity: O(log n)
class Solution(object):
    def sumAndMultiply(self, n):
        s=str(n)
        x=""
        tot=0
        for i in s:
            if i!="0":
                x=x+i
                tot+=int(i)
        if x=="":
            return 0
        r=int(x)*tot
        return r
        

        
