class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = {}
        
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
            
        sort_freq = sorted(count, key=count.get, reverse=True)
        
        res = ""
        for char in sort_freq:
            res += char * count[char]
            
        return res