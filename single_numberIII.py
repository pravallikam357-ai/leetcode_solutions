class Solution(object):
    def singleNumber(self, nums):
        a=[]
        for i in nums:
            if nums.count(i)==1:
                a.append(i)
        return a
