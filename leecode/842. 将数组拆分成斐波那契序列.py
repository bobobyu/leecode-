from typing import *


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        sol:List[str] = []
        def split_S(remain_string: str):

            print(remain_string)

            remain_len: int = len(remain_string)
            sol_len: int = len(sol)

            if not remain_string and sol_len >= 3:
                return
            for i in range(1, len(remain_string)+1):
                sol_ = remain_string[:i]
                print(sol_)
                if sol_len < 2:
                    sol.append(sol_)
                    split_S(remain_string=remain_string[i + 1:])
                else:
                    if remain_len >= len(sol[-1]) and eval(sol[-1]) + eval(sol[-2]) == eval(sol_):
                        sol.append(sol_)
                        split_S(remain_string=remain_string[i + 1:])
                    sol.pop()
        split_S(remain_string=S)

S = Solution()
print(S.splitIntoFibonacci("123456579"))
