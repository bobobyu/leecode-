from clock import *


class Solution:
    def mylongestValidParentheses(self, s: str) -> int:
        self.max_length: int = 0
        self.s_length: int = len(s)
        self.next_move: int = 0
        index: int = 0

        while index < len(s) - 1:
            if (self.s_length - index) > self.max_length:
                if s[index] == '(':

                    match_index: int = index + 1
                    l: int = 1
                    r: int = 0
                    while match_index < self.s_length:

                        if l <= (self.s_length - index) // 2 and r <= l:

                            if s[match_index] == '(':
                                l += 1
                            else:
                                r += 1
                            if r == l:
                                self.max_length = max(l, self.max_length)
                                self.next_move = l

                            match_index += 1
                        else:
                            break

                    index += max(self.next_move * 2, 1)

                else:
                    index += 1
                # print(self.next_move, index)
                self.next_move = 0
            else:
                break

        return self.max_length * 2

    def stacklongestValidParentheses(self, s: str) -> int:
        bracket_stack: list = [-1]
        self.max_lengths: int = 0

        for index in range(len(s)):
            if s[index] == '(':
                bracket_stack.append(index)
            else:
                if bracket_stack[-1] != -1:
                    if s[bracket_stack[-1]] == '(':
                        bracket_stack.pop(-1)
                        self.max_lengths = max(self.max_lengths, index - bracket_stack[-1])
                    else:
                        bracket_stack.append(index)
                else:
                    bracket_stack.append(index)
        return self.max_lengths


s = Solution()
print(s.stacklongestValidParentheses(')('))
