# Problem: Convert integer to the sum of two no zero intergers
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math
# Language: Python

#  Problem Description:
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

#Given an integer n, return a list of two integers [a, b] where:

#a and b are No-Zero integers.
#a + b = n
#The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

#  Approach:
# Create an empty list l to store the answer.
#Try every possible value of a from 1 to n-1.
#Calculate:
  #b = n - a
#Convert both numbers into strings:
#stra = str(a)
#strb = str(b)
#Check whether either number contains digit 0.
#If neither contains 0, add a and b to the list.
#Return the list.
# ⚡ Time Complexity: O(n log n)
# ⚡ Space Complexity: O(1)
class Solution(object):
    def getNoZeroIntegers(self, n):
        l=[]
        for a in range(1,n):
            b=n-a
            stra=str(a)
            strb=str(b)
            if "0" not in stra and "0" not in strb:
                l.append(a)
                l.append(b)
                return l
        
