class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        
        min_hour = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            potential_hour = 0
            for pile in piles:
                if pile < mid:
                    potential_hour += 1
                else:
                    potential_hour += math.ceil(pile/mid)
            
            if potential_hour > h:
                left = mid + 1
            else:
                min_hour = mid
                right = mid - 1
                
     
        return min_hour
           
                
            