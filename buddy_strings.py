# Problem: Buddy Strings
# Platform: LeetCode
# Difficulty: Easy
# Topic: Hash tables,Strings
# Language: Python

#  Problem Description:
# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

#Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

#For example, swapping at indices 0 and 2 in "abcd" results in "cbad"
#  Approach:
# Traverse both strings and store indices where characters differ.
#If strings are already equal, return True only when there is at least one duplicate character.
#Otherwise, there must be exactly 2 mismatches, and swapping those characters in s should make it equal to goal..

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def buddyStrings(self, s, goal):

        if len(s) != len(goal):
            return False

        # Case 1: strings are already equal
        if s == goal:
            return len(set(s)) < len(s)

        diff = []

        # Find different positions
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        # Must be exactly 2 differences
        if len(diff) != 2:
            return False

        i, j = diff

        return s[i] == goal[j] and s[j] == goal[i]
