class Solution:
    
    def rev(self, s: List[str], i, n) -> List:
        # base case
        if i >= n:
            return s

        # recurrence relation (sortof) swap and move two ptr
        s[i], s[n] = s[n], s[i]
        self.rev(s, i+1, n-1)
        
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        self.rev(s, 0, len(s)-1)
        
        
     