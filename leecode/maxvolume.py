class Solution:
    def maxArea(self, height: list) -> int:
        start_point: int = 0
        end_point: int = len(height) - 1
        max_volume: int = 0
        while start_point < end_point:
            max_volume = max((end_point - start_point) * min(height[end_point], height[start_point]), max_volume)
            if height[end_point] <= height[start_point]:
                end_point -= 1
            else:
                start_point += 1
        return max_volume

s = Solution()
print(s.maxArea([1,8]))
