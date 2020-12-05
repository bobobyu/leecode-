from typing import *
from collections import *


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not ops:
            return 0
        score_stack: deque = deque()
        for i in ops:
            if i.isalnum():
                score_stack.append(int(i))
            elif i == 'C':
                score_stack.pop()
            elif i == 'D':
                score_stack.append(score_stack[-1]*2)
            elif i == '+':
                score_stack.append(score_stack[-1] + score_stack[-2])
        return sum(score_stack)