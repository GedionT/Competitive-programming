class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        dup = defaultdict(list)
        
        for path in paths:
            root = path.split(" ")[0]
            files = path.split(" ")[1:]
            
            for file in files:
                content = file.split("(")
                dup[content[1]].append(f'{root}/{content[0]}')
        
        ans = []
        for k in dup:
            if len(dup[k]) > 1:
                ans.append(dup[k])
        
        return ans