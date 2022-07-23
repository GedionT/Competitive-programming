class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        
        # go thru string and find start and end
        visited = {}
        for index, char in enumerate(s):
            if char not in visited:
                visited[char] = [index, index]
            else:
                visited[char][1] = index
        
        # create merged interval between ranges
        intervals = []
        for v in visited:
            # merge if overlap
            interval = visited[v]
            if intervals and interval[0] < intervals[-1][1]:
                intervals[-1][1] = max(intervals[-1][1], interval[1])
            else:
                intervals.append(interval)
        
        return [end-start+1 for start,end in intervals]
        
        
        

        
        