from heapq import *
from typing import *


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        heap: List[int] = [intervals.pop(0)[1]]

        for i in intervals:
            if i[1] <= heap[0]:
                heappop(heap)

            heappush(heap, i[1])
        return len(heap)
