# Problem: Jewels and Stones
# Platform: LeetCode
# Difficulty: Easy
# Topic: Hash tables,Strings
# Language: Python

#  Problem Description:
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

#Letters are case sensitive, so "a" is considered a different type of stone from "A"
#  Approach:
# check wether given in stones are in jewels then increase the count and return the final count
#  Time Complexity: O(n*m)
#  Space Complexity: O(1)
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in stones:
            if i in jewels:
                count=count+1
        return count
        
