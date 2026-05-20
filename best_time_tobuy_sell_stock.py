# Problem: Best time to buy and sell stock
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays,Dynamic programming
# Language: Python

#  Problem Description:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0..

#  Approach:
# We traverse the array only once.
#Keep track of the minimum stock price seen so far.
#For every price:
#Assume we sell on that day.
#Calculate profit using:

#profit=current price−minimum price so far

#Update the maximum profit whenever we get a larger profit.

#  Time Complexity: O(n)
#  Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)

            profit = price - min_price

            max_profit = max(max_profit, profit)

        return max_profit
