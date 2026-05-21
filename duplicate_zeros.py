# Problem: Duplicate zeros
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Two pointer
# Language: Python

#  Problem Description:
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

#Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
#  Approach:
# Traverse array using while
#If element is 0
#insert another 0
#remove last element to maintain size
#move index by 2
#Else move normally
#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        while i<len(arr):
           if arr[i]==0:
               arr.insert(i,0)
               arr.pop()
               i=i+2
           else:
            i=i+1
        return arr
