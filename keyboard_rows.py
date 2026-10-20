# Problem: Keyboard Rows
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Hash table ,Strings
# Language: Python

#  Problem Description:
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

#Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
#In the American keyboard:
#the first row consists of the characters "qwertyuiop",
#the second row consists of the characters "asdfghjkl", and
#the third row consists of the characters "zxcvbnm".

#  Approach:
# 1. Initialize an empty list result to store the valid words.
# Define three strings representing the keyboard rows:
   #f → first row: "qwertyuiop"
   # s → second row: "asdfghjkl"
   #t → third row: "zxcvbnm"
#Iterate through each word in words.
#Convert each word to lowercase using i.lower() so uppercase letters are handled correctly.
#Use all(ch in row for ch in i.lower()) to check whether every character belongs to a particular keyboard row.
#If all characters belong to any one row, append the original word to result.
#Return result.

#  Time Complexity: n=no.of rows l=max length of word O(nxl)
#  Space Complexity: O(nxl)
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        result=[]
        f="qwertyuiop"
        s="asdfghjkl"
        t="zxcvbnm"
        for i in words:
            if all(ch in f for ch in i.lower()):
                result.append(i)
            if all(ch in s for ch in i.lower()):
                result.append(i)
            if all(ch in t for ch in i.lower()):
                result.append(i)
        return result
