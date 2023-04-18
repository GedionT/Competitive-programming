class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        large = max(candies)
        
        res = []
        
        for candy in candies:
            if candy + extraCandies >= large:
                res.append(True)
            else:
                res.append(False)
                
        return res