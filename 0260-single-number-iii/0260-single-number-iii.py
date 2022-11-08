class Solution:
    def checkBit(self, n, i):
        return (n & (1<<i)) != 0
    
    def setBitPos(self, n):
        for i in range(32):
            if self.checkBit(n, i):
                return i
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = 0        
        for n in nums:
            xor ^= n
        
        setBit = self.setBitPos(xor)  
        n1 = n2 = 0
        
        for idx in range(len(nums)):
            if self.checkBit(nums[idx], setBit):
                n1^=nums[idx]
            else:
                n2^=nums[idx]
        
        return [n1, n2]
        