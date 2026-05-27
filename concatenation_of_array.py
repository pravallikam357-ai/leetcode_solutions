class Solution(object):
    def getConcatenation(self, nums):
        for i in range(1):
            nums.extend(nums)
        return nums
