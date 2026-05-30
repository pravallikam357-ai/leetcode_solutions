# Problem: RansomNote
# Platform: LeetCode
# Difficulty: Easy
# Topic: Hashtable,string,counting
# Language: Python

#  Problem Description:
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

#Each letter in magazine can only be used once in ransomNote.

#  Approach:
# The idea is to check whether every character in ransomNote appears in magazine at least as many times as needed.

#Loop through each character ch in ransomNote.
#Compare:
#magazine.count(ch) → frequency of ch in magazine
#ransomNote.count(ch) → frequency of ch needed
#If the available count is less than the required count, return False.
#If all characters satisfy the condition, return True.

#  Time Complexity: O(n×(m+n))
#  Space Complexity: O(1)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        for ch in ransomNote:
            if magazine.count(ch) < ransomNote.count(ch):
                return False

        return True
