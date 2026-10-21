# Problem: Excel Sheet Column Title
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math,Strings
# Language: Python

#  Problem Description:
#Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#  Approach:
# Initialize rev = "" to store the column title.
#Run a while n > 0 loop.
#Subtract 1 from n because Excel column numbering starts at 1, whereas modulo arithmetic works with 0 to 25.
#Calculate r = n % 26 to get the letter's position.
#Convert the position to a character using chr(65 + r), where ASCII 65 represents 'A'.
#Add the character to the front of rev.
#Update n = n // 26 to process the remaining value.
#Return rev when n becomes zero..
#  Time Complexity: O(log n)
#  Space Complexity: O(log n)
class Solution:
    def convertToTitle(self, n: int) -> str:
        rev=""
        while n>0:
            n=n-1
            r=n%26
            rev=chr(65+r)+rev
            n=n//26
        return rev
    
