class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        total_count = 0
        
        for i,v in enumerate(reversed(sorted(Counter(arr).values()))):
            total_count += v
            
            if total_count >= len(arr) // 2:
                return i+1
        
        return 0
