from typing import *
from collections import *
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums).items()
        x_ = []
        [heapq.heappush(x_, i) for i in x]
        # print(x_)
        return [i[0] for i in heapq.nlargest(n=k, iterable=x_, key=lambda x: x[1])]


s = Solution()
print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
