from clock import *


class Solution:
    def sortColors(self, nums: list) -> None:
        count_two: int = 0
        for i, _ in enumerate(nums):
            num = nums[i]
            if num == 2:
                count_two += 1
            elif num == 0:
                nums.insert(0, nums.pop(i))
            elif num == 1:
                nums[i], nums[i - count_two] = nums[i - count_two], nums[i]



a = Solution()
s = [2, 1, 0, 1]
a.sortColors(s)
print(s)
'''
2 0 2 1 1 0 1
0 2 2 1 1 0 1
0 2 2 1 1 0 1
0 1 2 2 1 0 1
0 1 1 2 2 0 1
'''
