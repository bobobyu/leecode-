from collections import Counter
from typing import List
from time import sleep


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S)==1:
            return S
        s_dict: Counter = Counter(S)
        if len(s_dict) == 1:
            return ''
        s_sort_key: List[str] = sorted(s_dict, key=lambda x: s_dict[x], reverse=True)
        s_sort_values: List[int] = [s_dict[i] for i in s_sort_key]
        split_list: List[List[str]] = [[s_sort_key[0]] for _ in range(s_sort_values[0])]
        residue_string = ''
        for i, j in enumerate(s_sort_key[1:]):
            residue_string += j*s_sort_values[i+1]
        print(residue_string)
        residue_string = list(residue_string)
        while residue_string:
            for i in range(len(split_list)):
                split_list[i].append(residue_string.pop(0))
                if not residue_string:
                    res = ''
                    for i in split_list:
                        res += ''.join(i)
                    if res[-1] == res[-2]:
                        return ''
                    else:
                        return res
s = Solution()
print(s.reorganizeString("bbb12312asdb"))
