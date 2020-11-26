class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict: dict = {}
        t_dict: dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        for i in s_dict.keys():
            if not t_dict.get(i) or t_dict[i] != s_dict[i]:
                return False
        return True
s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))