from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        s_dict: Counter = Counter(S)

        res: str = ''
        del_list: list = []
        while len(s_dict) > 1:
            for i in s_dict:
                if s_dict[i]:
                    res += i
                    s_dict[i] -= 1
                    if s_dict[i] == 0:
                        del_list.append(i)
            for i in del_list:
                del s_dict[i]
        print(res, s_dict)
        if not s_dict:
            return res
        item = s_dict.popitem()
        if item[-1] > 1:
            return ''
        else:
            return res+item[0]


s = Solution()
print(s.reorganizeString("vvvlo"))
