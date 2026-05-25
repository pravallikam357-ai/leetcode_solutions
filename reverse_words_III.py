# Problem: Reverse words in a string III
# Platform: LeetCode
# Difficulty: Easy
# Topic: Two pointers and strings
# Language: Python

#  Problem Description:
#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

#  Approach:
# Acces each word in a sentence and reverse it.

#  Time Complexity: O(n²)
#  Space Complexity: O(n)
class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        for i in range(len(s)):
            s[i]=s[i][::-1]
            x=" ".join(s)
        return x
