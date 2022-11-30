class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts = Counter(arr)
        seen = set()
                
        for count in counts:
            if counts[count] in seen:
                return False
            seen.add(counts[count])
        
        return True