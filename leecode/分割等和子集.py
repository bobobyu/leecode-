class Solution:
    def canPartition(self, nums: list) -> bool:
        nums.sort()
        left_sum: int = 0
        left_point: int = 0
        right_point: int = len(nums) - 1
        while left_point < right_point:
            left_sum += nums[left_point]
            if left_sum < nums[right_point]:
                left_point += 1
            elif left_sum == nums[right_point]:
                right_point -= 1
                left_point += 1
            else:
                return False
        return True


s = Solution()
print(s.canPartition([1, 2, 3, 6]))
