from typing import *
from _collections import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic: dict = {}
        [dic.setdefault(''.join(sorted(i)), []).append(i) for i in strs]
        return list(dic.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
