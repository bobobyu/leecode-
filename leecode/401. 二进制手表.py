from typing import *


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        clock_list: List[int] = [i for i in range(10)]
        sol: List[List[int]] = []
        invalid_set: Set[int] = set()
        last_in: int = clock_list[-1]

        def rec(sol_: List, n: int = num, alternative_list: List[int] = clock_list):
            if n == 0:
                sol.append(sol_)

            else:
                for i, j in enumerate(alternative_list):
                    if not sol_ or j > sol_[-1]:
                        rec(n=n - 1, alternative_list=alternative_list[:i] + alternative_list[i + 1:], sol_=sol_ + [j])

        rec(sol_=[])
        [print(i) for i in sol]


s = Solution()
s.readBinaryWatch(3)
