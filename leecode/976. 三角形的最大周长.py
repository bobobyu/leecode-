from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        def judge_triangle(nums: List[int]) -> int:
            a, b, c = nums
            return sum(nums) if all([a + b > c, a + c > b, b + c > a]) else 0

        A.sort()
        point: int = len(A)
        while point > 2:
            # print(A[point - 3:point], point)
            if max_perimeter := judge_triangle(nums=A[point - 3:point]):
                return max_perimeter
            point -= 1
        return 0


s = Solution()
print(s.largestPerimeter([3,6,2,3]))
