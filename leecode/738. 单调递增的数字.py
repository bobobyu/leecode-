from typing import *


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n_string: str = str(N)
        self.IF: bool = False
        self.sol_: int = 0
        first = eval(n_string[0])
        length: int = len(n_string)

        def dfs(remain: str, sol: str, limit: list, eq: bool, layer: int):
            if self.IF:
                return
            if len(sol) <= length:
                if not remain:
                    if (s := sol.lstrip('0')) != '' and (s_ := eval(s)) <= N:
                        # print(eval(sol.lstrip('0')), ';')
                        self.sol_ = s_
                        self.IF = True
                    return
                ll = len(remain)
                # print(remain, sol, limit)
                if layer == 0:
                    for i in range(limit[1], limit[0] - 1, -1):
                        if i == eval(remain[0]):
                            dfs(remain[1:], sol + str(i), [i, eval(remain[1 if (ll != 1) else 0])], True, layer + 1)
                        else:
                            dfs(remain[1:], sol + str(i), [i, 9], False, layer + 1)
                elif eq:
                    for i in range(limit[1], limit[0] - 1, -1):
                        if i == eval(remain[0]):
                            # print(remain[1 if (ll != 1) else 0], remain, ll)
                            dfs(remain[1:], sol + str(i), [i, eval(remain[1 if (ll != 1) else 0])], True, layer + 1)
                        else:
                            dfs(remain[1:], sol + str(i), [i, 9], False, layer + 1)
                else:
                    for i in range(limit[1], limit[0] - 1, -1):
                        dfs(remain[1:], sol + str(i), [i, 9], False, layer + 1)

        dfs(remain=n_string, sol='', limit=[0, first], eq=False, layer=0)
        return self.sol_


print(Solution().monotoneIncreasingDigits(100))
