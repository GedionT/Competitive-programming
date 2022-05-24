class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        def merge(word1, word2):
            if not word1:
                return word2
            if not word2:
                return word1
            if word1[0] < word2[0]:
                return word1[0] + merge(word1[1:], word2)
            else:
                return word2[0] + merge(word1, word2[1:])
        
        return merge(word1, word2)