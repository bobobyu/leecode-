from typing import *


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if set(nums) == {0}:
            return 1
        if (l := len(nums)) <= 2:
            return l
        length: int = 1
        flag: int = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] < 0 and (flag == 1 or flag == 0):
                flag = -1
                length += 1
            elif nums[i] - nums[i - 1] > 0 and (flag == -1 or flag == 0):
                flag = 1
                length += 1

        return length


print(Solution().wiggleMaxLength([0,0]))
