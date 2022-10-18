class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(n: int) -> str:
        
            left = right = 0
            n = list(str(n))
            sol = ''

            while right < len(n)-1:
                if n[left] == n[right]:
                    right += 1

                if n[left] != n[right]:
                    sub = right-left  
                    sol += str(sub)+str(n[left])
                    left = right


            sol += str(right-left+1)+str(n[left])

            return sol
        
        last = "1"
        for i in range(1, n):
            last = helper(int(last))
        
        return last