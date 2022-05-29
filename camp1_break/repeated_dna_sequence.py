class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeat = set(), set()
        
        
        for l in range(len(s) - 9):
            curr = s[l: l+10]
            
            if curr in seen:
                repeat.add(curr)
                
            seen.add(curr)
        
        
        return list(repeat)