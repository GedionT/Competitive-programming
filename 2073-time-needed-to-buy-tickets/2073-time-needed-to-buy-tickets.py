class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        num = tickets[k]
        res = 0
        
        for i in range(k+1):
            res += min(tickets[i],num)
            
        for i in range(k+1,len(tickets)):
            res += min(tickets[i],num-1)
            
        return res