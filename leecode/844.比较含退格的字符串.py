class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_length = len(S)
        t_length = len(T)
        stack = []
        for i in range(s_length):
            if S[i] == '#' and stack:
                stack.pop(-1)
            elif S[i] != '#':
                stack.append(S[i])
        s = ''.join(stack)
        stack.clear()
        for i in range(t_length):
            if T[i] == '#' and stack:
                stack.pop(-1)
            elif T[i]!='#':
                stack.append(T[i])
        t =''.join(stack)
        return s==t
s = Solution()
print(s.backspaceCompare("y#fo##f",
"y#f#o##f"))
