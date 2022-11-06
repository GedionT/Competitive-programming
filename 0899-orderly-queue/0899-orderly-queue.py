class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:        
        if k == 1:
          
            lex_small = s
            s = list(s)

            for idx in range(len(s)):
                to_shift = max(s[0:k])  
                s.pop(s.index(to_shift))
                s.append(to_shift)

                lex_small = min(lex_small, "".join(s))

            return lex_small
        
        else:
             return "".join(sorted(s))

