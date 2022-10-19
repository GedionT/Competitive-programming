class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        line_length = float('-inf')
        
        for vals in ranges:
            line_length = max(line_length, vals[1])
            
        if left > line_length or right > line_length:
            return False
            
        line = [0]*(line_length + 2)
               
        for val in ranges:
            line[val[0]] += 1
            line[val[1]+1] -= 1
        
        line = line[1:-1]
        
        prefix = [0]
        for point in line:
            prefix.append(prefix[-1] + point)
            
        prefix = prefix[1:]
        for i in range(left-1, right): 
            if prefix[i] <= 0:
                return False
        
        return True
            
        