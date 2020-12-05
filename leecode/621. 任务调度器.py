from typing import *
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        t_count: Counter = Counter(tasks)
        tasks_lip: List[str] = sorted(t_count.keys(), key=lambda x: t_count[x], reverse=True)
        main_ = tasks_lip.pop(0)
        task_seq: List[List[str]] = [[main_] for _ in range(t_count[main_])]
        remain_list: List[str] = [i * t_count[i] for i in tasks_lip]
        remain_list = list(''.join(remain_list))
        timer: int = 0



s = Solution()
print(s.leastInterval(
    tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
