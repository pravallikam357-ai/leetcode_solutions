class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            char = strs[0][i]

        # Compare with all other strings
            for s in strs[1:]:
            # Check index out of range or mismatch
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
