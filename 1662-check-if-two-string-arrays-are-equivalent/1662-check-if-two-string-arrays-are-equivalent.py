class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return self.buildString(word1) == self.buildString(word2)

        
    def buildString(self, word: List[str]) -> str:
        return ''.join(word)