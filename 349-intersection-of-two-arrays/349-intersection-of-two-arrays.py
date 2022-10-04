class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            num1, num2 - intersection?
            unique and no order 
           
           1 2 2 1     2 2 
           
           1: 1       
           2: 3
        """
        
        intersec = {}
        
        for num in nums1:
            if num not in intersec:
                intersec[num] = 1
        
        ans = []
        for num in nums2:
            if num in intersec and num not in ans:
                ans.append(num)
                
        return ans