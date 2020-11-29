from typing import List
from collections import deque


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length: int = len(nums)
        prefix_list: List[int] = [0] * length
        prefix_list[0] = nums[0]
        # suffix_list: List[int] = [0] * length
        # suffix_list[-1] = nums[-1]
        for i in range(1, length + 1):
            prefix_list[i - 1] = min(nums[i - 1], prefix_list[max(0, i - 2)])
            # suffix_list[-i] = min(nums[-i], suffix_list[min(-i + 1, -1)])
        # print(f'{prefix_list}\n{nums}\n')
        s: deque = deque([nums[-1]])
        for i in range(length - 2, 0, -1):
            if nums[i] > prefix_list[i-1]:
                while s and s[0] <= prefix_list[i-1]:
                    s.popleft()
                if s and nums[i] > s[0]:
                    return True
                s.appendleft(nums[i])
        return False



s = Solution()
print(s.find132pattern([3,5,0,3,4]
                       ))
