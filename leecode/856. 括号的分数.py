from typing import Deque
from collections import deque


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        score_stack: Deque[int] = deque()
        s = list(S)
        while s:
            # print(score_stack, '     ',s[0])
            if s.pop(0) == '(':
                score_stack.append(0)
            else:
                score: int = 0
                if score_stack[-1] == 0:
                    score_stack[-1] = 1
                    continue
                while score_stack[-1] != 0:
                    score += score_stack.pop()
                score_stack[-1] = 2 * score
        return sum(score_stack)

s = Solution()
print(s.scoreOfParentheses("(()(()))"))