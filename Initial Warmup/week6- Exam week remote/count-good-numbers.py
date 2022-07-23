class Solution:
    def countGoodNumbers(self, n: int) -> int:

#         n = 1 -> 5
#         0, 2, 4, 6, 8
        
#         n = 4 -> 400
#         0123
        
        
#         n = 50 -> 564908303
        
        

        # even count based on len
        if n%2==0:
            even=n//2
        else:
            even=(n+1)//2
            
        # odd count
        odd=n//2

        mod = 10**9+7
        
        tot_even_combination = pow(5,even, mod)      
        tot_odd_combination = pow(4,odd, mod)    
        
        return (tot_even_combination * tot_odd_combination) % mod
        