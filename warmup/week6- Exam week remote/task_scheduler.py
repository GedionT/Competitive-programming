from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        count_table = {}
        
        for t in tasks:
            if t in count_table:
                count_table[t] += 1
            else:
                count_table[t] = 1
        
        lst_count = sorted(count_table.values(), reverse=True)
        
        max_number = lst_count[0]
        
        counter = 0
        i = 0
        
        while i < len(lst_count) and lst_count[i] == max_number:
            counter += 1
            i+= 1
        
        ret = (max_number - 1) * (n+1) + counter
        
        return max(ret, len(tasks))