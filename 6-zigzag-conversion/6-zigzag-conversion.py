class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        cur_row, down = 0, 0

        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows-1:
                down ^= 1
            cur_row += 1 if down else -1
        
        return ''.join([row for row in rows])