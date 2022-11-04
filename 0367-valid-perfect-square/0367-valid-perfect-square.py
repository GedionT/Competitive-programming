class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        print(math.sqrt(num))
        if (math.sqrt(num) * 10) % 10 == 0:
            return True
        
        return False