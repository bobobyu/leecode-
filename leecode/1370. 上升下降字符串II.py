from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        s_count: Counter = Counter(s)
        s_keys: list = sorted(list(s_count.keys()))

        res = ''

        while sum(s_count.values()):
            for i in s_keys:
                if s_count[i]:
                    res += i
                    s_count[i] -= 1
            if sum(s_count.values()):
                for i in s_keys[::-1]:
                    if s_count[i]:
                        res += i
                        s_count[i] -= 1
        return res

s = Solution()
print(s.sortString(""))

