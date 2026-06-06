class Solution:
    def reverseVowels(self, s):
        v = [c for c in s if c in "aeiouAEIOU"][::-1]
        i = 0
        return "".join(v.pop(0) if c in "aeiouAEIOU" else c for c in s)
