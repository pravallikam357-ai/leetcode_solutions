# Problem: Reverse number
# Platform: LeetCode
# Difficulty: Medium
# Topic: Math
# Language: Python

#  Problem Description:
# Find the reverse of the given number.

#  Approach:
# Acces the last digits and add it to reverse.

# ⚡ Time Complexity: O(n)
# ⚡ Space Complexity: O(1)
import math
class Solution(object):
    def reverse(self, x):
        s=-1 if x<0 else 1
        x=abs(x)
        rev=0
        while x>0:
            d=x%10
            x=x//10
            rev=rev*10+d
            if rev>(2**31)-1:
                return 0
        return s*rev
        
