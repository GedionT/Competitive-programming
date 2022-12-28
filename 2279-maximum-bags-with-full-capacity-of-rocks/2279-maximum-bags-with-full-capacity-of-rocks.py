class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        for idx in range(len(capacity)):
            capacity[idx] = capacity[idx] - rocks[idx]
            
        capacity.sort()
        
        count = 0
        for cap in capacity:
            if cap <= additionalRocks:
                count += 1
                additionalRocks -= cap
            
        return count
        
        