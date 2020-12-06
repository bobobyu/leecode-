from typing import *


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        alternative_: List[str] = [str(i) for i in range(10)]

        self.count_ = 0

        def rec(n, alt, sol):
            if n == 0:
                # if len(set(sol)) != len(sol):
                #     print(sol)
                self.count_ += 1
            else:
                for i, j in enumerate(alt):
                    if ((sol and sol[-1] == '0') or (not sol)) and j == '0':
                        rec(n - 1, alt=alt, sol=sol + [j])
                    else:
                        rec(n - 1, alt=alt[:i] + alt[i + 1:], sol=sol + [j])

        rec(n, alternative_, [])

        return self.count_


s = Solution()
print(s.countNumbersWithUniqueDigits(3))
print(s.countNumbersWithUniqueDigits(2))

