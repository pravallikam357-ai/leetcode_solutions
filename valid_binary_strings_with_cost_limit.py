# Problem: Valid Binary Strings with cost limit
# Platform: LeetCode
# Difficulty: Medium
# Topic: Arrays
# Language: Python

#  Problem Description:
# You are given two integers n and k.

#The cost of a binary string s is defined as the sum of all indices i (0-based) such that s[i] == '1'.

#A binary string is considered valid if:
#It does not contain two consecutive '1' characters.
#Its cost is less than or equal to k.
#Return a list of all valid binary strings of length n in any order.
#  Approach:
# This solution uses backtracking (DFS) to generate all binary strings of length n.

#Parameters of dfs:

#i → current index being filled.
#prev → previous character placed.
#cost → accumulated cost so far.
#cur → current string being built.
#  Time Complexity: O(Fn+2​)≈O(1.618n)
#  Space Complexity: O(n)
class Solution(object):
    def generateValidStrings(self, n, k):
        ans = []

        def dfs(i, prev, cost, cur):
            if cost > k:
                return

            if i == n:
                ans.append("".join(cur))
                return

            # Place 0
            cur.append('0')
            dfs(i + 1, '0', cost, cur)
            cur.pop()

            # Place 1
            if prev != '1':
                cur.append('1')
                dfs(i + 1, '1', cost + i, cur)
                cur.pop()

        dfs(0, '0', 0, [])
        return ans
