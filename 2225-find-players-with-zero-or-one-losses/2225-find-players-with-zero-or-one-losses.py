class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        win_count = {}
        loss_count = {}
        
        for match in matches:
            if match[0] in win_count:
                win_count[match[0]] += 1
            else:
                win_count[match[0]] = 1
                
            if match[1] in loss_count:
                loss_count[match[1]] += 1
            else:
                loss_count[match[1]] = 1
                
             
        first = []
        second = []
        for win in win_count:
            if win not in loss_count:
                first.append(win)
        
        for loss in loss_count:
            if loss_count[loss] == 1:
                second.append(loss)
        
        return [ sorted(first), sorted(second) ]