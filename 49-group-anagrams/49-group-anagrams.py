class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        match = defaultdict(list)
        
        for i, st in enumerate(strs):
            match[''.join(sorted(st))].append(i)

        ans = []
        
        for m in match:
            temp = []
            for idx in match[m]:
                temp.append(strs[idx])
            ans.append(temp)
        
        return ans