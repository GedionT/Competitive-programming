class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = ''.join(map(str, digits))
        d = int(l)+1
        ans = list(map(int, list(str(d))))
        return ans