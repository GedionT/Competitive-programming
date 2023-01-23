class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:     
        """
            1: 3                
            2: 3
            3: 6
            5: 6, 7
            4: 5, 8, 9
            10: 4, 9

            WINS(len(graph))   LOSS(count in values of all keys)
            1:  1                0
            2:  1                0
            3:  1                2
            4:  3                1
            5:  2                1
            10: 2                0
            6:                   2
            7:                   1
            8:                   1
            9:                   2

            result = [[1, 2, 10], [4, 5, 7, 8]]
        """ 
        
        loss_count = {}
        
        for winner, loser in matches:
            loss_count[winner] = loss_count.get(winner, 0)
            loss_count[loser] = loss_count.get(loser, 0) + 1
        
        no_loss, one_loss = [], []
        for player, count in loss_count.items():
            if count == 0:
                no_loss.append(player)
            if count == 1:
                one_loss.append(player)
                
        return [sorted(no_loss), sorted(one_loss)]
        