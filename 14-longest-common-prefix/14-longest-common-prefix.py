class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        _min = sys.maxsize
        
        for s in strs:
            _min = min(_min, len(s))
        
        res = ""
        
        for i in range(_min):
            ch = strs[0][i]
            for s in strs:
                if s[i] != ch:
                    return res
                
            res += ch
        
        return res