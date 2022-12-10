class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        freq_list = [ (-count[x], x) for x in count ]
        
        heapq.heapify(freq_list)
        
        result = []
        
        while k:
            freq, num = heapq.heappop(freq_list)
            result.append(num)
            k -= 1
            
        return result