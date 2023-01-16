class Solution:
#     def hasOverlap(self, interval_1: List[int], interval_2: List[int]) -> bool:
#         a1, b1 = interval_1
#         a2, b2 = interval_2
        
#         return min(a1, a2) - max(b1, b2) >= 0
    
#     def mergeInterval(self, interval_1: List[int], interval_2: List[int]) -> List:
#         a1, b1 = interval_1
#         a2, b2 = interval_2
        
#         new Interval = [ min(a1, a2), max(b1, b2) ]
        
#         return newInterval
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        pos = bisect.bisect(intervals, newInterval)
        intervals.insert(pos, newInterval)
    
        res = []
        
        for i in range(len(intervals)):
            if not res or intervals[i][0] > res[-1][1]:
                    res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                
        return res
                                                          