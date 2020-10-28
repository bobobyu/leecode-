class Solution:
    def permute(self, nums: list) -> list:
        nums = [[i] for i in nums]
        result = []

        def dp(nums: list, res: list):
            if len(nums) == 1:
                result.append(res + nums[0])
            for i in range(len(nums)):
                dp(nums=nums[0:i]+nums[i+1:], res=res + nums[i])

        dp(nums, res=[])
        return result


s = Solution()
print(s.permute([1,1,2]))
