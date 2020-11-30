from typing import List, DefaultDict



class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        static: List[int] = [0, -float('inf'), -float('inf')]
        for i in nums:
            print(static)
            a, b, c = static

            if i % 3 == 0:
                static[0] += i
                static[1] += i
                static[2] += i

            elif i % 3 == 1:

                static[0] = max(static[0], c + i)
                static[1] = max(static[1], a + i)
                static[2] = max(static[2], b + i)

            else:

                static[0] = max(static[0], b + i)
                static[1] = max(static[1], c + i)
                static[2] = max(static[2], a + i)

        return static[0]


s = Solution()
s.maxSumDivThree(
    [5, 2, 2, 2])
