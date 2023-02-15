class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = ""
        while n > 0:
            n -= 1
            res = chr(n % 26 + ord('A')) + res
            n //= 26
        return res