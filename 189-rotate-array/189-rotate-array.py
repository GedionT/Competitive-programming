class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        [ nums.insert(0, nums.pop()) for i in range(k) ]
           