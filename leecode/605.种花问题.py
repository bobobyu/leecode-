class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        for i, j in enumerate(flowerbed):
            if n == 0:
                return True
            if not j and not flowerbed[max(0, i-1)] and not flowerbed[min(len(flowerbed)-1, i+1)]:
                n -= 1
                flowerbed[i] = 1
        if n:
            return False
        return True
s = Solution()
print(s.canPlaceFlowers( flowerbed = [0,0,1,0,0], n = 1))
