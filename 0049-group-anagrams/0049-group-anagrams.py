class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)
        
        for st in strs:  
            group[''.join(sorted(st))].append(st)
        
        
        return group.values()
            