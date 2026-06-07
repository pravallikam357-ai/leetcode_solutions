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
