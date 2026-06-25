class Solution(object):
    def sortedSquares(self, nums):
        l=[]
        for i in range(len(nums)):
            sq=nums[i]**2
            l.append(sq)
        l.sort()
        return l
        
