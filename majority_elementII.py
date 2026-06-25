# Problem: Majority Element II
# Platform: LeetCode
# Difficulty: Medium
# Topic: Arrays,Hashtable,Sorting,Counting
# Language: Python

#  Problem Description:
# Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times

#  Approach:
# Create a dictionary count to store the frequency of each number.
#Traverse the array once:
#For every number, increase its count.
#count.get(num, 0) + 1 means:
#If num exists → take its current count
#If not → start from 0
#Add 1
#Traverse the dictionary:
#Check which numbers appear more than n/3 times.
#Add those numbers to ans.

#  Time Complexity: O(n)
#  Space Complexity: O(n)
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
