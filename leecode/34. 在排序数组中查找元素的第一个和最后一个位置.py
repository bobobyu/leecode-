from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        not_find: List[int] = [-1, -1]
        if not nums or target > nums[-1] or target < nums[0] :
            return not_find

        def dichotomy_search(low: int, high: int):
            if low == high and nums[low] != target:
                return -1
            middle: int = (low + high) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return dichotomy_search(low=middle + 1, high=high)
            elif nums[middle] > target:
                return dichotomy_search(low=low, high=middle - 1)

        length: int = len(nums)
        index_: int = dichotomy_search(low=0, high=length - 1)
        if index_ == -1:
            return not_find
        start_point: int = index_
        end_point: int = index_
        while start_point > 0 and nums[start_point - 1] == target:
            start_point -= 1
        while end_point < length - 1 and nums[end_point + 1] == target:
            end_point += 1
        return [start_point, end_point]


s = Solution()
print(s.searchRange([],
6))
