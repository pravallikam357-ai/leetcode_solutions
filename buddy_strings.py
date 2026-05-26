class Solution(object):
    def buddyStrings(self, s, goal):

        if len(s) != len(goal):
            return False

        # Case 1: strings are already equal
        if s == goal:
            return len(set(s)) < len(s)

        diff = []

        # Find different positions
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        # Must be exactly 2 differences
        if len(diff) != 2:
            return False

        i, j = diff

        return s[i] == goal[j] and s[j] == goal[i]
