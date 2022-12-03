class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = {}
        
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
           
        heap = []
        
        for char, freq in count.items():
            heapq.heappush(heap, (-freq, char))
            
            
        ans = ''
        while heap:
            frq, char = heapq.heappop(heap)
            ans += char * (-frq)
            
        return ans
        