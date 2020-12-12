from typing import *


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if set(nums) == {0}:
            return 1
        elif (l := len(nums)) <= 2:
            return l
        length: int = 1
        sign: int = 0
        for i in range(1, len(nums)):
            if sign == 0:
                if (diff := nums[i] - nums[i - 1]) == 0:
                    continue
                sign = 1 if diff > 0 else -1
                length += 1
            elif nums[i] - nums[i - 1] < 0 and sign > 0:
                length += 1
                sign *= -1
            elif nums[i] - nums[i - 1] > 0 and sign < 0:
                length += 1
                sign *= -1
        return length


print(Solution().wiggleMaxLength([1, 1, 7, 4, 9, 2, 5]))
