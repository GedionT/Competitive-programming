class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = len(nums1) + len(nums2)
        first = second = 0
        merged = []
        
        while first < len(nums1) and second < len(nums2):
            if nums1[first] <= nums2[second]:
                merged.append(nums1[first])
                first += 1
                
            elif nums1[first] > nums2[second]:
                merged.append(nums2[second])
                second += 1
                
        while first < len(nums1):
            merged.append(nums1[first])
            first += 1
            
        while second < len(nums2):
            merged.append(nums2[second])
            second += 1
            
        if n % 2 == 0:
            return (merged[n//2] + merged[(n//2)-1]) / 2
        
        return merged[n//2] 