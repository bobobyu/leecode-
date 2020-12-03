from collections import Counter
from typing import List


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = Counter(s)
        stack: List[str] = []
        for i in s:
            d[i] -= 1
            if i not in stack:
                while stack and i <= stack[-1] and d[stack[-1]]:
                    stack.pop(-1)
                stack.append(i)
        return ''.join(stack)


s = Solution()
print(s.removeDuplicateLetters(s="cbacdcbc"))
