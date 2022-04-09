class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0) or (flowerbed[0] == 1 and n == 0):
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                print(n)
                flowerbed[i] = 1
                n -= 1
                print(n)
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        return False