class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(candidate, weights, days):
            current_weight = 0 
            days_taken = 1
            
            for weight in weights:
                current_weight += weight
                
                if current_weight > candidate:
                    days_taken += 1
                    current_weight = weight
                    
            return days_taken <= days
        
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right-left) // 2   
            if canShip(mid, weights, days):
                right = mid
            else:
                left = mid + 1
                
        return right
    
        

              
                