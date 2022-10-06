class TimeMap:

    def __init__(self):
        self.time_series = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_series[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:            
        sub = self.time_series[key]
        
        # alt one: move from r to left
        # for i in range(len(sub)-1, -1, -1):
        #     if sub[i][0] <= timestamp:
        #         return sub[i][1]
        
        left = 0
        right = len(sub)
        
        while left < right:
            mid = (left+right)//2
            if self.time_series[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        return "" if right == 0 else self.time_series[key][right-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)