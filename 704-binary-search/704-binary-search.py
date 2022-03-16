class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        
        while left <= right:
            
            mid = left + (right-left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                if left == right:
                    return left
                return left + 1
            
        
        return -1
    