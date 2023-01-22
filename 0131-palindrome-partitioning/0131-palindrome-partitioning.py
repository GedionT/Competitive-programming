class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        
        self.dfs(s, 0, [])
        
        return self.res
    
    
    def isPalindrome(self, string, start_idx, end_idx):
        
        while start_idx <= end_idx:
            if string[start_idx] != string[end_idx]:
                return False
            
            start_idx += 1
            end_idx -= 1
            
        return True
    
    
    def dfs(self, string, start_idx, path):
        
        if start_idx >= len(string):
            self.res.append(path)
            
        for l in range(len(string) - start_idx):
            if self.isPalindrome(string, start_idx, start_idx + l):
                self.dfs( string, start_idx + l + 1, path + [string[ start_idx : start_idx + l + 1]] )
                         
                         
        