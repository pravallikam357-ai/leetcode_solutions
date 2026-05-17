# Problem: Longest Common Prefix
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,strings
# Language: Python

# Problem Description:
# Find the longest common prefix in a given list of strings.

#  Approach:
# Take the first string as the reference string.
#Traverse each character of the first string.
#Compare that character with the character at the same index in all other strings

#characters mismatch, or
#index exceeds any string length

#then return the prefix found till now.

#If all characters match, return the entire first string.
#  Time Complexity: O(n*m)
#  Space Complexity: O(1)
class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            char = strs[0][i]

        # Compare with all other strings
            for s in strs[1:]:
            # Check index out of range or mismatch
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
