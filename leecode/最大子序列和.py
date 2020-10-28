class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sum: int = nums[0]
        start_point: int = 0
        end_point: int = 1
        current_list: list = [nums[0]]
        l_length: int = len(nums)
        while end_point < l_length:
            current_sum = sum(current_list)
            if current_sum + nums[end_point] >= nums[end_point]:
                max_sum = max(current_sum + nums[end_point], max_sum)
                current_list = nums[start_point:end_point + 1]
            else:
                start_point = end_point
                current_list = [nums[start_point]]
                max_sum = max(max_sum, nums[start_point])
            end_point += 1
        return max_sum
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,5,4]))