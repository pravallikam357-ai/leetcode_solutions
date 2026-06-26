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
        
