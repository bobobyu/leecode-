from typing import List


class Solution:

    def __init__(self):
        self.sol = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        def two_sum(point_: int, target_: int):
            # print(nums[point_:], target_)
            hash_: set = set()
            sol:set = set()
            for i in range(point_, length):

                tag: int = target_ - nums[i]
                # print(hash_, tag, nums[i], i==length-1)
                if tag in hash_ and tag not in sol:
                    self.sol.append([-target_, tag, nums[i]])
                    sol.add(tag)
                hash_.add(nums[i])

        point: int = 0
        while point < length:
            while point < length - 1 and nums[point] == 0 and nums[point + 1] == 0:
                point += 1
            two_sum(point_=point + 1, target_=0 - nums[point])
            point += 1
            while point < length and nums[max(point - 1, 0)] == nums[point]:
                point += 1
            # print()

        return self.sol + [[0, 0, 0]] if nums.count(0) >= 3 else self.sol


s = Solution()
print(s.threeSum([0,0,0]))
