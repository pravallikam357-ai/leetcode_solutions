# Problem: Unique no.of ocuurences
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hashtable
# Language: Python

#  Problem Description:
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

#  Approach:
# The goal is to check whether the frequency of each number in arr is unique.

#Convert arr to a set to get unique elements.
#For each unique element:
#Find its frequency using arr.count(i).
#Store the frequency in counts.
#After adding a frequency, compare:
#len(counts) → total frequencies found so far
#len(set(counts)) → unique frequencies
#If they are not equal, a frequency is repeated, so return False.
#If the loop completes, all frequencies are unique, so return True.
#  Time Complexity:O(n²)
#  Space Complexity: O(n)
class Solution(object):
    def uniqueOccurrences(self, arr):
        counts=[]
        for i in set(arr):
            count=arr.count(i)
            counts.append(count)
            if len(counts)!=len(set(counts)):
                return False
        return True
