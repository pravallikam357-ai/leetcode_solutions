# Problem: Intersection of two arrays
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtable,twopointers,sorting,BinarySearch
# Language: Python

#  Problem Description:
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

#  Approach:
# Create an empty list l.
#Traverse each element in nums1.
#Check:
#if the element exists in nums2
#and it is not already in l
#If both are true, add it to l.
#Return l as the intersection array.

#  Time Complexity: O(n²)
#  Space Complexity: O(n)
class Solution(object):
    def intersection(self, nums1, nums2):
        l=[]
        for i in nums1:
            if i in nums2 and i not in l:
                l.append(i)
        return l
