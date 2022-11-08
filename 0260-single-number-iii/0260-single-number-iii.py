class Solution:
    def checkBit(self, n, i):
        return (n & (1<<i))!=0
    
    def setBitPos(self, n):
        # return xor & -xor
        for i in range(32):
            if self.checkBit(n, i):
                return i
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = 0        
        for n in nums:
            xor ^= n
        
        setBit = self.setBitPos(xor)  
        x1, x2 = 0, 0
        
        for i in range(len(nums)):
            if self.checkBit(nums[i], setBit):
                x1^=nums[i]
            else:
                x2^=nums[i]
        
        return [x1, x2]
        