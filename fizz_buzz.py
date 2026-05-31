# Problem: Fizz Buzz
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math,Strings,Simulation
# Language: Python

#  Problem Description:
# Given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.
 
#  Approach:
#The goal is to generate a list from 1 to n:

#If a number is divisible by 3 and 5, add "FizzBuzz".
#If divisible by 3 only, add "Fizz".
#If divisible by 5 only, add "Buzz".
#Otherwise, add the number itself as a string..

#  Time Complexity: O(n)
#  Space Complexity: O(n)
class Solution(object):
    def fizzBuzz(self, n):
        answers=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                answers.append("FizzBuzz")
            elif i%3==0:
                answers.append("Fizz")
            elif  i%5==0:
                answers.append("Buzz")
            else:
                answers.append(str(i))
        return answers

        
