class Solution(object):
    def lengthOfLastWord(self, s):
        splits=s.split()
        return len(splits[-1])
        
