class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        r = ""

        while i >= 0 or j >= 0 or c > 0:
            a_d = int(a[i]) if i >= 0 else 0
            b_d = int(b[j]) if j >= 0 else 0

            t = a_d + b_d + c
            d = t % 2
            c = t // 2

            r = str(d) + r

            j -= 1
            i -= 1

        return r
