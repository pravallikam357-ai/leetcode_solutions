
#program: LeetCode
# Difficulty: Easy
# Topic: Hashtable,math,string
# Language: Python

#  Problem Description:
# Convert the given roman number to integer.

#  Approach:
# For each character:

#If the current value is less than the next value, subtract it.
#Example: "IV" → I < V → subtract 1
#Otherwise, add it..

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def romanToInt(self, s):
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        integer=0
        for i in range(len(s)):
                if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                       integer -= roman[s[i]]
                else:
                    integer += roman[s[i]] 
        return integer
