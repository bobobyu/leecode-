from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(set(nums)) == 1 and nums[0] == 0:
            return
        length: int = len(nums)
        point = 0
        while length:
            if nums[point] == 0:
                nums.append(nums.pop(point))
            else:
                point += 1
            length -= 1
s = Solution()
num = [0,0,0,0,0]
s.moveZeroes(num)
print(num)