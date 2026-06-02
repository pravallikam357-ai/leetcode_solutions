class Solution(object):
    def findDisappearedNumbers(self, nums):
        s=set(nums)
        a=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                a.append(i)
        return a
