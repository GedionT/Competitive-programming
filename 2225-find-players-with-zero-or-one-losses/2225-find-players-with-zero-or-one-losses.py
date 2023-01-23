class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:     
        
        loss_count = [-1] * 100001
        
        for winner, loser in matches:
            if loss_count[winner] == -1:
                loss_count[winner] = 0
            
            if loss_count[loser] == -1:
                loss_count[loser] = 1
            else:
                loss_count[loser] += 1
                
        answer = [[], []]
        for i in range(100001):
            if loss_count[i] == 0:
                answer[0].append(i)
            elif loss_count[i] == 1:
                answer[1].append(i)
                
        return answer
        