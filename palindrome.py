import math
class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        rev=y[::-1]
        if rev==y:
             return True
        else:
            return False
