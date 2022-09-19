class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        # sanity check
        if len(changed) % 2:
            return []
        
        count = Counter(changed)
        changed.sort()
        
        ans = []
        
        
        for num in changed:
            if num == 0 and count[0] >= 2:
                count[0] -= 2
                ans.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1  
                ans.append(num)
        
        return ans if len(ans) == len(changed)// 2 else []
    
    
    
# #        shorter code with cleaner conditional 
#         c = collections.Counter(changed)
        
#         if c[0] % 2:
#             return []
        
#         for x in sorted(c):
#             if c[x] > c[2 * x]:
#                 return []
#             c[2 * x] -= c[x] if x else c[x] // 2
            
#         return list(c.elements())
        