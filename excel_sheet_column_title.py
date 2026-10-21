class Solution:
    def convertToTitle(self, n: int) -> str:
        rev=""
        while n>0:
            n=n-1
            r=n%26
            rev=chr(65+r)+rev
            n=n//26
        return rev
    
