class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        
        # sanity check 1
        if len(word) > ROWS*COLS: 
            return False
        
        # sanity check 2
        board_char_count = Counter([ board[i][j] for i in range(ROWS) for j in range(COLS)])
        word_char_count = Counter(word)
        
        for ch, freq in word_char_count.items():
            if board_char_count[ch] < freq:
                return False
        
        
        directions = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
        inbound = lambda x, y: 0 <= x < ROWS and 0 <= y < COLS
        
        def dfs_backtrack(r, c, idx):
            if idx == len(word):
                return True
           
            temp = board[r][c]
            board[r][c] = ""
            
            for dx, dy in directions:
                nx, ny = r+dx, c+dy
                if inbound(nx, ny) and board[nx][ny] == word[idx]:
                    if dfs_backtrack(nx, ny, idx+1) == True:
                        return True
                
            board[r][c] = temp
            return False

            
        # start search on every node
        for idx in range(ROWS):
            for jdx in range(COLS):
                if board[idx][jdx] == word[0] and dfs_backtrack(idx, jdx, 1):
                    return True
                
        return False