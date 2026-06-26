# Problem: Intersection of two Arrays
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtable,Two pointers,Binary search and sorting
# Language: Python

#  Problem Description:
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

#  Approach:
# Create an empty list l to store the intersection values.
#Traverse each element i in nums1.
#Check if i exists in nums2.
#If it exists:
#Add it to the answer list.
#Remove that occurrence from nums2 so duplicates are handled correctly.
#Return the result list.

#  Time Complexity: O(n × m)
#  Space Complexity: O(min(n, m))
class Solution(object):
    def intersect(self, nums1, nums2):
        l = []

        for i in nums1:
            if i in nums2:
                l.append(i)
                nums2.remove(i)

        return l
