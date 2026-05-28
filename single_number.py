class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
           count=nums.count(i)
           if count==1:
               return i 
