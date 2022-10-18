class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        _max = float('-inf')
        
        for trip in trips:
            _max = max(_max, trip[2])
            
        line = [0] * (_max+1)
        
        
        for trip in trips:
            line[trip[1]] += trip[0]
            line[trip[2]] -= trip[0]
            
        
        prefix = [0]
        
        for i in range(len(line)):
            prefix.append(prefix[-1]+line[i])
            

        for i in range(1, len(prefix)):
            if prefix[i] > capacity:
                return False
        
        return True