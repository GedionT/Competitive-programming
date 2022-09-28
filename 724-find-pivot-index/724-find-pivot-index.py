class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        ltr_pre = [0]
        rtl_pre = [0]
        
        for idx in range(len(nums)): 
            ltr_pre.append(nums[idx]+ltr_pre[-1])
            
        for idx in range(len(nums)-1, -1, -1):
            rtl_pre.append(nums[idx]+rtl_pre[-1])
        
        rtl_pre.reverse()
        
        ltr_pre = ltr_pre[1:]
        rtl_pre = rtl_pre[0:len(rtl_pre)-1]
        
        for i in range(len(ltr_pre)):
            if ltr_pre[i] == rtl_pre[i]:
                return i
        
        return -1
        