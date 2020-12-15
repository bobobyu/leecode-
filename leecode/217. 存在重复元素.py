from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = 0
        for i in nums:
            if i < 0:
                sign = -1
            else:
                sign = 0
            if m == 0:
                m = 1 << (2 * abs(i) + sign)
            else:
                # print(bin(m), bin(1 << 2 * abs(i) + sign), i, 2 * abs(i) + sign)
                if m & (mm := 1 << (2 * abs(i) + sign)):
                    # print(bin(m))
                    return True
                else:
                    m |= mm

        return False


print(Solution().containsDuplicate(nums=[1, 5, -2, -4, 0]))
