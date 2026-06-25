class Solution(object):
    def majorityElement(self, nums):
        count = {}
        ans = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key in count:
            if count[key] > len(nums)//3:
                ans.append(key)

        return ans
