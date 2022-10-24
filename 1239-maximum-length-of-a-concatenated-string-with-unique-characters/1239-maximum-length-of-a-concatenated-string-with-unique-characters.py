class Solution:
    def solve(self, words: List[str], index: int, word: ''):
        if len(word) != len(set(word)):
            return
        
        self.ans = max(self.ans, len(word))
        
        if index == len(words):
            return
        
        for i in range(index, len(words)):
            self.solve(words, i+1, word+words[i])
    
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        self.solve(words=arr, index=0, word='')
        
        return self.ans