class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        f=1
        s=2
        for i in range(3,n+1):
            c=f+s
            f=s
            s=c
        return s
        
