from typing import *


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        clock_list: List[int] = [i for i in range(10)]
        sol: List[List[int]] = []

        def rec(sol_: List, n: int = num, alternative_list: List[int] = clock_list):
            if n == 0:
                sol.append(sol_)

            else:
                for i, j in enumerate(alternative_list):
                    if not sol_ or j > sol_[-1]:
                        rec(n=n - 1, alternative_list=alternative_list[:i] + alternative_list[i + 1:], sol_=sol_ + [j])

        rec(sol_=[])
        res: List[str] = []
        for i in sol:
            hours: List[str] = ['0', 'b'] + ['0'] * 4
            minutes: List[str] = ['0', 'b'] + ['0'] * 6
            for j in i:
                if j <= 3:
                    hours[j + 2] = '1'
                else:
                    minutes[j - 2] = '1'
            if (hour := eval(''.join(hours))) <= 11 and (minute := eval(''.join(minutes))) <= 59:
                res.append(f"{str(hour)}:{str(minute).rjust(2, '0')}")
        return res

s = Solution()
print(s.readBinaryWatch(1))
