class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        count = [0] * len(word)
        
        for i in range(len(word)):
            if word[i].isupper():
                count[i] = 1 

        if sum(count) == len(word) or sum(count) == 0: # all upper and lower
            return True
        
        if count[0] == 1 and sum(count) == 1:
            return True
        
        else:
            False