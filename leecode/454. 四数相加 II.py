from typing import List, Set
from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        a_b: List[int] = [i + j for i in A for j in B]
        c_d:Counter = Counter([i + j for i in C for j in D])
        count_: int = 0
        for i in a_b:
            count_ += c_d.get(-i, 0)
        return count_


s = Solution()
print(s.fourSumCount([-1, -1],
                     [-1, 1],
                     [-1, 1],
                     [1, -1],
                     ))
