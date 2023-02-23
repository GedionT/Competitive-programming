class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        m = {}
        return self.dfs(expression, m)
        
    def dfs(self, exprn, m):
        if exprn in m:
            return m[exprn]
        if exprn.isdigit():
            m[exprn] = int(exprn)
            return [int(exprn)]
        
        ret = []
        for i, c in enumerate(exprn):
            if c in "+-*":
                l = self.diffWaysToCompute(exprn[:i])
                r = self.diffWaysToCompute(exprn[i+1:])
                ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[exprn] = ret
        return ret