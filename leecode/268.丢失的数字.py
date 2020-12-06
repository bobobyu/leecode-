from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s |= i << 1
        s = eval('0b' + ''.join(['1' if i == '0' else '1' for i in bin(s)[2:].ljust(len(nums), '0')])) | 0
        return s

s = Solution()
print(s.missingNumber([3,0,1]))