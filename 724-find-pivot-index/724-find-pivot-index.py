class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        ltr_pre = [0]
        rtl_pre = [0]
        
        for idx in range(len(nums)-1): 
            ltr_pre.append(nums[idx]+ltr_pre[-1])
            
        for idx in range(len(nums)-1, 0, -1):
            rtl_pre.append(nums[idx]+rtl_pre[-1])
        
        rtl_pre.reverse()

        for i in range(len(ltr_pre)):
            if ltr_pre[i] == rtl_pre[i]:
                return i
        
        return -1
        