class Solution(object):
    def runningSum(self, nums):
        run=0
        l=[]
        for i in range(len(nums)):
            run=run+nums[i]
            l.append(run)
        return l
        
