class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            values = []
            for i in range(1, (n // 2) + 1):
                values.extend([i])
                values.insert(0, -1 * i)
            return values
        else:
            values = [0]
            for i in range(1, (n // 2) + 1):
                values.extend([i])
                values.insert(0, -1 * i)
            return values