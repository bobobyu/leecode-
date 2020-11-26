from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        s: list = list(s)
        s_count: Counter = Counter(s)
        s_set = sorted(s_count.keys())
        res = ''
        while s:
            for i in s_set:
                s_count[i] -= 1
                if not s_count[i]:
                    del s_count[i]
                    s_set.remove(i)
                s.remove(i)
                res += i

            if s:
                for i in s_set[::-1]:
                    s_count[i] -= 1
                    if not s_count[i]:
                        del s_count[i]
                        s_set.remove(i)
                    s.remove(i)
                    res += i
        return res
s =Solution()
print(s.sortString("aaaabbbbcccc"))