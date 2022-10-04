class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            num1, num2 - intersection?
            unique and no order 
           
           1 2 2 1     2 2 
           
           1: 1       
           2: 3
        """
        
        n1 = set(nums1)
        n2 = set(nums2)
        
        return list(n1 & n2)