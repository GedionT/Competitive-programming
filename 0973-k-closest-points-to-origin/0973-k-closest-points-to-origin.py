class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sqrt/ x2 + y2
        
        equclidistance = [0] * len(points)
        for idx in range(len(points)):
            x, y = points[idx]
            equclidistance[idx] = (sqrt(pow(x, 2) + pow(y, 2)), idx)
            
        heapq.heapify(equclidistance)
        
        res = []
        while k:
            dist, i = heapq.heappop(equclidistance)
            res.append(points[i])
            k -= 1
            
        return res