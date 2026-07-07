# Problem: Remove Duplicates from sorted array
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Two pointers
# Language: Python

#  Problem Description:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

#Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

#The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

#  Approach:
# Assume the first element is unique, so set i = 1.
#Traverse the array using j.
#If nums[j] is different from the last unique element (nums[i-1]):
#Copy nums[j] to nums[i].
#Increment i.
#After the loop, the first i elements contain all unique values.
#Return i (the number of unique elements).

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        i=1
        for j in range(1,len(nums)):
            if nums[j]!=nums[i-1]:
                nums[i]=nums[j]
                i+=1
        return i
