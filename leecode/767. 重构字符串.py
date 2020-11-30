from collections import Counter
from typing import List


class Solution:
    def reorganizeString(self, S: str) -> str:
        s_dict: Counter = Counter(S)
        s_sort_key: List[int] = sorted(s_dict, key=lambda x: s_dict[x], reverse=True)
        res: str = ''
        split_list: List[int] = []
        for i in s_
        print(s_dict, s_sort_key)
        print(split_list)

s = Solution()
print(s.reorganizeString("vvvaalo"))

