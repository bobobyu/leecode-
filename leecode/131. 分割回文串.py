from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol: List[List[str]] = []
        size: int = len(s)

        def check_(string: str):
            if not string:
                return False
            start_point = 0
            end_point = len(string) - 1
            while start_point < end_point:

                if string[start_point] != string[end_point]:
                    return False
                start_point += 1
                end_point -= 1
            return True

        def rec(low: int, sol_: List[str]):
            if low == size:
                sol.append(sol_)
            for i in range(low, size+1):
                if check_(_sol := s[low:i]):
                    # print(_sol)
                    rec(low=i, sol_=sol_ + [_sol])

        rec(low=0, sol_=[])
        return sol


s = Solution()
print(s.partition("aab"))
'acccaccca'
