class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        
        for i in range(len(startTime)):
            jobs.append( (startTime[i], endTime[i], profit[i]) )
            
        jobs.sort(key = lambda job: job[0])
        memo = [-1] * len(jobs)
        
        for idx,job in enumerate(jobs):
            startTime[idx] = job[0]
        
        def findMaxProfit(memo, pos):
           
            if pos == len(memo):
                return 0
            if memo[pos] != -1:
                return memo[pos]
            
            nextIndex = bisect_left(startTime, jobs[pos][1]) # equivalent to lower_bound of c++
            maxProfit = max(findMaxProfit(memo, pos+1), jobs[pos][2]+findMaxProfit(memo, nextIndex))
            memo[pos] = maxProfit
            
            return maxProfit
        
        return findMaxProfit(memo, 0)