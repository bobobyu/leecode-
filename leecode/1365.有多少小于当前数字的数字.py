class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        nums_ = nums[:]
        nums.sort()
        start: int = 0
        end: int = 0
        res: dict = {}
        # print(nums)
        while end < len(nums):
            while end < len(nums) and nums[max(0, end-1)] == nums[end]:
                end += 1
            res[nums[start]] = start
            if end == len(nums) - 1:
                res[nums[-1]] = end
                break
            start = end
            end += 1
        return [res[i] for i in nums_]

s = Solution()
print(s.smallerNumbersThanCurrent([7,7,7]))
