class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                # print(i)
                for k in range(len(nums) - 1, i-1, -1):
                    if nums[i-1] < nums[k]:
                        # print(i, k)
                        nums[i-1], nums[k] = nums[k], nums[i-1]
                        nums[i:] = nums[i:][::-1]
                        return
        nums.reverse()


s = Solution()
nums = [3,2,1]
s.nextPermutation(nums)
print(nums)
