from typing import *


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map_: List[List[int]] = [[0 if (i > 0 and j > 0) else 1 for j in range(m)] for i in range(n)]
        for row in range(1, n):
            for col in range(1, m):
                map_[row][col] = map_[row][col - 1] + map_[row - 1][col]

        # [map_[row][col] := map_[row][col - 1] + map_[row - 1][col] for col in range(1, m) for row in range(1, n)]
        return map_[-1][-1]


print(Solution().uniquePaths(7, 3))
