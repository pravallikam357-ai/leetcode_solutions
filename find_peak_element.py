# Problem: Find Peak Element
# Platform: LeetCode
# Difficulty: Medium
# Topic: Arrays,Binary search
# Language: Python

#  Problem Description:
#A peak element is an element that is strictly greater than its neighbors.

#Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

#You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

#You must write an algorithm that runs in O(log n) time.
#  Approach:
# Initialize two pointers:
  #l = 0
  #r = len(nums) - 1
#While l < r:
#Find the middle index.
#Compare nums[mid] with nums[mid + 1].
#If nums[mid] > nums[mid + 1], move the right pointer to mid.
#Otherwise, move the left pointer to mid + 1.
#When l == r, that index is a peak.
#Return l.

#  Time Complexity: O(log n)
#  Space Complexity: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[mid+1]:
                r=mid
            else:
                l=mid+1
        return l
