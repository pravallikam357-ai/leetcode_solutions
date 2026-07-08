class Solution(object):
    def sumAndMultiply(self, n):
        s=str(n)
        x=""
        tot=0
        for i in s:
            if i!="0":
                x=x+i
                tot+=int(i)
        if x=="":
            return 0
        r=int(x)*tot
        return r
        

        
