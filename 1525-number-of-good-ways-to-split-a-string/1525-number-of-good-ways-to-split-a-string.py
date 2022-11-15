class Solution:
    def numSplits(self, s: str) -> int:
                        
        def fixes(lst):
            f_set = set()
            fix = [0]

            for c in lst:
                if c not in f_set:
                    f_set.add(c)
                    fix.append(fix[-1]+1)
                else:
                    fix.append(fix[-1])
                    
            return fix
        
        pre = fixes(s)[1:]
        post = fixes(s[::-1])[::-1]
        
        post = post[:-1]
        

        count = 0
        for i in range(len(pre)-1):
            if pre[i] == post[i+1]:
                count += 1
                
        return count
            
                
                