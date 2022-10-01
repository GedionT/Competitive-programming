import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        # expand buildings to account for the start and end of each building.
        # a tuple is an end of building if height = 0
        buildings = sorted(
            [(start, -height, end) for start, end, height in buildings] +
            [(end, 0, None) for _, end, _ in buildings]
        )
        
        # print(buildings)
        
        # intialize heap and res
        heap, res = [(0, inf)], [(0, 0)]
        
        
        # iterate through all buildings
        for start, height, end in buildings:
            
            # if building ends before current start, remove it from heap
            while start >= heap[0][1]:
                heapq.heappop(heap)
                
                
            # if current height is greater than 0 add it along with current end to heap
            if height:
                heapq.heappush(heap, (height, end))
                
            # find the max height
            maxHeight = -heap[0][0]
            
            # if curr max height is different form previous max height, add curr start and max height to res
            if maxHeight != res[-1][1]:
                res.append([start, maxHeight])
                
        return res[1:]