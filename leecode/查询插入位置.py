class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        nums_length: int = len(nums)
        for index in range(len(nums)):
            if nums[index] >= target:
                return index
        return nums_length

s =Solution()
print(s.searchInsert([1,2,3,4],0))