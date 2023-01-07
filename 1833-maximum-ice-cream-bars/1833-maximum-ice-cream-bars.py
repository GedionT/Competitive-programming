class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        n =  len(costs)
        count = 0
        
        while count < n and coins >= costs[count]:
            coins -= costs[count]
            count += 1
        
        return count