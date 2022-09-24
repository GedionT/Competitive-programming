class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        """
            prices of indexed shop
            
            discount indexed by j i.e minimum index such that j > i
            and prices[j] <== prices[i]
            
            return answer list where ans[i] = final price you pay for ith item
            considering the special discount
            
            
            e.g [8, 4, 6, 2, 3] ->  [4, 2, 4, 2, 3]
            
                [1 2 3 4 5]     ->  [1 2 3 4 5]
            
                [10 1 1 6]      ->  [9 0 1 6]
                
        # Bruteforce with O(n^2) time and o(1 space)    
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        
        return prices
        
        
        # monotonic stack with o(n) space and time
        p [8-4, 4 6 2 3]
        s [0, ]
        """
          
        
        stack = []
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                prices[stack.pop()] -= p
            stack.append(i)
            
        return prices
        
