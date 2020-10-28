class Solution:
    def removeDuplicates(self, nums: list) -> int:
        start_point: int = 0
        end_point: int = 1
        while end_point <= len(nums) - 1:
            while nums[start_point] == nums[end_point]:
                nums.pop(start_point)
                if end_point == len(nums):
                    return len(nums)
            start_point += 1
            end_point += 1
        return len(nums)


s = Solution()
a = [1, 1,2,2]
s.removeDuplicates(a)
print(a)
