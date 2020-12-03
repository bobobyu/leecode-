from collections import Counter, deque

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        num_counter: Counter = Counter(s)
        stack: deque = deque()
        invalid_set: set = set()
        for let in s:
            num_counter[let] -= 1
            if let not in invalid_set:
                while stack and (pre_ := stack[-1]) >= let and num_counter[pre_]:
                    stack.pop()
                    invalid_set.discard(pre_)
                stack.append(let)
                invalid_set.add(let)
        return ''.join(stack)
