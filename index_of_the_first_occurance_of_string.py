class Solution(object):
    def strStr(self, haystack, needle):
        n=len(haystack)
        m=len(needle)
        if m>n:
            return -1
        for i in range(0,n-m+1):
            j=0
            while j<m and haystack[i+j]==needle[j]:
                j=j+1
            if j==m:
                return i
        return -1
