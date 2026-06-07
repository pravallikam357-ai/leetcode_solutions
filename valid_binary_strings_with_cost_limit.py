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
