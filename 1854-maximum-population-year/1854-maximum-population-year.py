class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
            1950   +1
            1960   +1
            1961   -1
            1970   +1
            1971   -1
            1981   -1
        """
        
        sweep = defaultdict(int)
        
        for start, end in logs:
            sweep[start] += 1
            sweep[end] -= 1
  
        max_year = 0
        max_amt = 0
        prefix = 0
        for key in sorted(sweep):
            prefix += sweep[key]
            
            if prefix > max_amt:
                max_year = key
                max_amt = prefix
        
        return max_year