from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.count_: int = 0

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.nums = nums.copy()

        def merge_(low: int, high: int) -> List[int]:
            if low == high:
                return [self.nums[low]]
            middle = (low + high) >> 1
            l: List[int] = merge_(low=low, high=middle)
            r: List[int] = merge_(low=middle + 1, high=high)
            l_r: List[int] = []
            r_length: int = len(r)
            l_length: int = len(l)
            l_point: int = 0
            r_point: int = 0

            while l_point < l_length and r_point < r_length:
                if l[l_point] > r[r_point] << 1:
                    self.count_ += l_length - l_point
                    r_point += 1
                else:
                    l_point += 1

            while r and l:
                if l[0] < r[0]:
                    l_r.append(l.pop(0))
                else:
                    l_r.append(r.pop(0))
            while l:
                l_r.append(l.pop(0))
            while r:
                l_r.append(r.pop(0))
            return l_r

        merge_(0, len(nums) - 1)
        return self.count_


s = Solution()
print(s.reversePairs([2, 4, 3, 5, 1]))
