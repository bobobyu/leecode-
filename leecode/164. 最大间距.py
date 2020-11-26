from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if  len(nums)<2:
            return 0
        max_, min_ = -float('inf'), float('inf')
        for i in nums:
            max_ = max(i, max_)
            min_ = min(i, min_)
        sort_nums: List[int] = [0] * (max_ - min_+1)
        for j in nums:
            sort_nums[j - min_] = 1
        pre_point: int = 0
        next_point: int = 0
        max_dis_ = -float('inf')
        length = len(sort_nums)
        while pre_point < length and next_point < length:
            while pre_point<length and  not sort_nums[pre_point]:
                pre_point += 1
            next_point = pre_point+1
            while next_point < length and not sort_nums[next_point]:
                next_point += 1
            max_dis_ = max(next_point - pre_point, max_dis_)
            pre_point += 1
        return max_dis_

s = Solution()
print(s.maximumGap([3,6,9,1]))