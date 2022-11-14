class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True

class Solution:    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        results = []
        
        trie = TrieNode()
        for word in words:
            trie.add_word(word)
        
        def dfs(r, c, node, word):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                board[r][c] == " " or board[r][c] not in node.children):
                return
            temp_char = board[r][c]
            board[r][c] = " "
            node = node.children[temp_char]
            word += temp_char
            
            if node.is_word:
                results.append(word)
                node.is_word = False
            
            if not node.children:
                del node
            else:
                dfs(r + 1, c, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r, c - 1, node, word)
            
            board[r][c] = temp_char
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")
        return results