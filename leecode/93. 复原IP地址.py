from typing import *


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        sol_list: Set[str] = set()

        def dfs(remain: str, sol: list, length: int):
            if not remain and length == 4:
                # print(sol)
                sol_list.add('.'.join(sol))
            if length < 4:
                for i in range(1, 4):
                    # print(sol, remain, remain[:i])
                    if (string := remain[:i])  and (string[0] != '0' or len(string) == 1) and eval(
                            string) <= 255:
                        dfs(remain=remain[i:], sol=sol + [remain[:i]], length=length + 1)

        dfs(remain=s, sol=[], length=0)
        return list(sol_list)


print(Solution().restoreIpAddresses("010010"))
