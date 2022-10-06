class TimeMap:

    def __init__(self):
        self.time_series = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_series[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:            
        sub = self.time_series[key]
        
        for i in range(len(sub)-1, -1, -1):
            if sub[i][0] <= timestamp:
                return sub[i][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)