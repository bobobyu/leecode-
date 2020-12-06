from collections import *
import heapq
from typing import *

class Solution:
    def frequencySort(self, s: str) -> str:
        s_: Counter = Counter(s)
        heap: List[int] = []
        for i in s_.items():
            heapq.heappush(heap, i)
        res = ''
        for i in heapq.nlargest(iterable=heap,n=len(heap), key=lambda x:x[1]):
            res = res + i[0]*i[1]
        return res

s = Solution()
print(s.frequencySort("tree"))
