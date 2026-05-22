class Solution(object):
    def removeTrailingZeros(self, num):
        num=int(num)
        d=num%10
        while d==0:
            num=num//10
            d=num%10
        return str(num)
