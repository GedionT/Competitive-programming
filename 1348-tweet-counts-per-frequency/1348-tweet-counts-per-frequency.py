class TweetCounts:

    def __init__(self):
        self.hashmap = {}     

    def recordTweet(self, tweetName: str, time: int) -> None:
        if(tweetName not in self.hashmap):
            self.hashmap[tweetName] = [time]
        else:
            self.hashmap[tweetName].append(time)
    
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        times = self.hashmap[tweetName]
        
        size = 0 
        secs = 0
        
        if(freq == 'minute'):
            secs = 60
            size = (endTime - startTime) / 60 + 1
        if(freq == 'hour'):
            secs = 3600
            size = (endTime - startTime) / 3600 + 1
        if(freq == 'day'):
            secs = 86400
            size = (endTime - startTime) / 86400 + 1
                
        r = [0] * int(size)
        
        for i in times:
            if(startTime <= i and i <= endTime):
                index = int((i-startTime)/secs)
                r[index] += 1

        return r

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)