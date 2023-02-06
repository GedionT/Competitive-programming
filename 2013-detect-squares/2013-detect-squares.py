class DetectSquares:

    def __init__(self):
        self.sweep = {}
        
    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.sweep:
            self.sweep[tuple(point)] = 0
        self.sweep[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0 
        px,py = point
        for x,y in self.sweep.keys():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if (x,py) in self.sweep and (px,y) in self.sweep:
                res += self.sweep[(x,py)] * self.sweep[(px,y)] * self.sweep[(x,y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)