class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
            
        def backtrack(substr="", i=0):
            if len(substr) == len(s):
                res.append(substr)
            else:
                if s[i].isalpha():
                    backtrack(substr + s[i].swapcase(), i + 1)
                backtrack(substr + s[i], i + 1)
                
        backtrack()
        return res