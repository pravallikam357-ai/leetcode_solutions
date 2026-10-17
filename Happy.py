# Problem: Happy Number
# Platform: LeetCode
# Difficulty: Easy
# Topic: Hash table,Math,Two pointer,Floyd's cycle Finding Algorithm
# Language: Python

#  Problem Description:
# Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not

#  Approach:
# Initialize an empty set seen to store previously visited numbers.
#While n is not equal to 1:
# If n is already in seen, return False because a cycle exists.
# Add n to seen.
# Initialize s = 0.
# Extract each digit using n % 10.
# Add the square of each digit to s.
# Remove the last digit using n // 10.
# Update n = s.
#If n becomes 1, return True

#  Time Complexity: O(1)
#  Space Complexity: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            s = 0
            while n >= 1:
                l = n % 10
                s = s + l**2
                n = n // 10
            n = s
        return True
