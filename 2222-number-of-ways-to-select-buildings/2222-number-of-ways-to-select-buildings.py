class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        
        # build the prefix
        z_prefix = [0] * (n+1)
        o_prefix = [0] * (n+1)
        
        for i in range(n):
            if s[i] == '0':
                z_prefix[i+1] = z_prefix[i] + 1
                o_prefix[i+1] = o_prefix[i]
            else:
                o_prefix[i+1] = o_prefix[i] + 1
                z_prefix[i+1] = z_prefix[i]

        
        # iterate over and calculate count
        count = 0
        for i in range(1, n-1):
            if s[i] == '1':
                left_z = z_prefix[i+1]
                right_z = z_prefix[-1] - left_z
                count += left_z * right_z
            else:
                left_o = o_prefix[i+1]
                right_o = o_prefix[-1] - left_o
                count += left_o * right_o
                
        return count


        