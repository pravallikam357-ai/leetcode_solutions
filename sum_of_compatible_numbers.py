# Problem: Sum of compatible Numbers in range i
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays
# Language: Python

#  Problem Description:
# You are given two integers n and k.

#A positive integer x is called compatible if it satisfies both of the following conditions:

#abs(n - x) <= k
#(n & x) == 0
#Return the sum of all compatible integers x.

#  Approach:
# The function considers all integers in the range:

#[n−k,n+k]

#(with the left boundary at least 1).

#For each number left in this range, it checks:

#(n & left) == 0
#The bitwise AND of two numbers is 0 only when they do not share any set bits in common.

#If the condition is true, that number is added to the sum a.
#Steps:
#Set left = max(1, n-k).
#Set right = n+k.
#Traverse every number from left to right.
#If (n & current_number) == 0, add it to the answer.
#Return the final sum.
#  Time Complexity: O(k)
#  Space Complexity: O(1)
class Solution(object):
    def sumOfGoodIntegers(self,n,k):
        left=max(1,n-k)
        right=n+k
        a=0
        while left<=right:
            if (n&left)==0:
                a+=left
            left+=1
        return a
