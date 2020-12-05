from typing import *
from collections import *


class Solution:
    def reverseParentheses(self, s: str) -> str:
        string_stack: Deque = deque()
        s = list(s)
        while s:
            if (op := s.pop(0)) == '(':
                string_stack.append('(')
            elif op == ')':
                temp: str = ''
                while string_stack[-1] != '(':
                    temp = string_stack.pop() + temp
                string_stack[-1] = temp[::-1]
            else:
                string_stack.append(op)
        return ''.join(string_stack)
s = Solution()
print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))