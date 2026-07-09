class Solution(object):
    def addDigits(self, num):
        while num>=10:
            tot=0
            while num>0:
                l=num%10
                tot+=l
                num=num//10
            num=tot
        return num
        
