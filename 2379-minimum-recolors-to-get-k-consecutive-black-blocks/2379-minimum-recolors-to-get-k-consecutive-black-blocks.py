class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_wCount = k
        
        
        # current range and white count in the range
        start = 0
        end = 0
        w_inWindow = 0

        
        # extend sliding window until criteria is met
        while end < len(blocks):
            # add count of w in window
            if blocks[end] == 'W':
                w_inWindow += 1

            # expand till condition met  
            if end - start + 1 < k:
                end += 1
            
            # condition is met, so recalc
            elif end - start + 1 == k:
                min_wCount = min(min_wCount, w_inWindow)
                
                if blocks[start] == 'W':
                    w_inWindow -= 1
                    
                start += 1
                end += 1
                
        return min_wCount
        