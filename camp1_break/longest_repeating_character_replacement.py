class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = l = maxFreq = 0
        
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])
            
            
            while (r-l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
        
            res = max(res, r-l + 1)
        
        return res


        # AABBABA ; k = 2

        # Brute force:

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if len(set(s[i:j+1])) == len(s[i:j+1]):
        #             res = max(res, j-i+1)
        # return res
        

        """
        
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        # Approach 2: Sliding Window
        # Time Complexity: O(n)
        # Space Complexity: O(1)


        """

  