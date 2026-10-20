class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        result=[]
        f="qwertyuiop"
        s="asdfghjkl"
        t="zxcvbnm"
        for i in words:
            if all(ch in f for ch in i.lower()):
                result.append(i)
            if all(ch in s for ch in i.lower()):
                result.append(i)
            if all(ch in t for ch in i.lower()):
                result.append(i)
        return result
