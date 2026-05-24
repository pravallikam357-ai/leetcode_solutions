# Problem: Detect Capital
# Platform: LeetCode
# Difficulty: Easy
# Topic: Strings
# Language: Python

#  Problem Description:
# We define the usage of capitals in a word to be right when one of the following cases holds:

#All letters in this word are capitals, like "USA".
#All letters in this word are not capitals, like "leetcode".
#Only the first letter in this word is capital, like "Google".
#Given a string word, return true if the usage of capitals in it is right.

 

#  Approach:
# Check each word by  wether it is captital or not by using isupper(),islower() functions if it is right return True otherwise False.

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def detectCapitalUse(self, word):
        if word[0].isupper() and word[1:].islower():
            return True
        elif word.isupper():
            return True
        elif word.islower():
            return True  
        else:
            return False 
