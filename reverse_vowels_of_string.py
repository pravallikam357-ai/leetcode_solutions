# Problem: Reverse vowels of a string
# Platform: LeetCode
# Difficulty: Easy
# Topic: Two pointers,strings
# Language: Python

#  Problem Description:
#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#  Approach:
# Extract all vowels from the string into a list.
#Reverse the list of vowels.
#Traverse the original string:
#If the current character is a vowel, replace it with the next vowel from the reversed list.
#Otherwise, keep the character unchanged.
#Join all characters to form the final string

#  Time Complexity: O(n²)
#  Space Complexity: O(n)
class Solution:
    def reverseVowels(self, s):
        v = [c for c in s if c in "aeiouAEIOU"][::-1]
        i = 0
        return "".join(v.pop(0) if c in "aeiouAEIOU" else c for c in s)
