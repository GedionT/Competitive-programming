class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        count = Counter(tasks)
        
        rounds = 0
        for times in count.values():
            
            if times == 1:
                return -1
            
            if times % 3 == 0:
                rounds += times // 3

            else:
                rounds += times // 3 + 1

        return rounds
                 