class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_wise = defaultdict(set)
        col_wise = defaultdict(set)

        squares = defaultdict(set) 
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row_wise[r] or
                    board[r][c] in col_wise[c] or
                    board[r][c] in squares[((r//3, c//3))]):
                    return False
                
                
                col_wise[c].add(board[r][c])
                row_wise[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                
        return True