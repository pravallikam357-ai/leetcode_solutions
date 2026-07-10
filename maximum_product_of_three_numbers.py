class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        n=len(nums)
        pro1=nums[n-1]*nums[n-2]*nums[n-3]
        pro2=nums[0]*nums[1]*nums[n-1]
        if pro1>pro2:
            return pro1
        else:
            return pro2
