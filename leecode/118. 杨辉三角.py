from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol: List[List[int]] = []
        for i in range(1, numRows + 1):
            # print(sol)
            if i <= 2:
                sol.append([1] * i)
            else:
                new_row: List[int] = [1, 1]
                for j in range(len(sol[i-2]) - 1):
                    new_row.insert(j + 1, sol[i-2][j] + sol[i-2][j + 1])
                sol.append(new_row)
        return sol

s = Solution()

print(s.generate(5))