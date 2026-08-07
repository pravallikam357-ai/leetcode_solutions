# Problem: Valid paranthesis
# Platform: LeetCode
# Difficulty: Easy
# Topic: String,stack,bracket sequence
# Language: Python

#  Problem Description:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#  Approach:
# Create an empty stack.
#Traverse the string from left to right.
#If the character is an opening bracket (, [, {:
#Push it into the stack.
#If it is a closing bracket:
#If the stack is empty → False
#Check whether the top of the stack is its matching opening bracket.
#If not matching → False
#If matching → pop it.
#After traversing the entire string:
#If the stack is empty → True
#Otherwise → False

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
