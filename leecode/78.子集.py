from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(nums_list: list):
            if nums_list:
                if nums_list not in res:
                    res.append(nums_list)
                    for i, j in enumerate(nums_list):
                        rec(nums_list[:i]+nums_list[i+1:])
        rec(nums_list=nums)
        res.append([])
        return res

s = Solution()
print(s.subsets([1, 2, 3]))
