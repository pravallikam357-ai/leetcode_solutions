# Problem: Climbing Stairs
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math,Dynamic programming,Memoization
# Language: Python

#  Problem Description:
# You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#  Approach:
# To reach stair n, you can:
#Take 1 step from stair n-1.
#Take 2 steps from stair n-2.
#So, the recurrence relation is:
   #dp[n]=dp[n−1]+dp[n−2]

#Instead of storing the entire dp array, the solution keeps only the last two computed values.
#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        f=1
        s=2
        for i in range(3,n+1):
            c=f+s
            f=s
            s=c
        return s
        
