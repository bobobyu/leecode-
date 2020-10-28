class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}': '{', ']': '[', ')': '('}
        count_: list = []
        for i in s:
            if i in ['(', '[', '{']:
                count_.append(i)
                continue
            if count_:
                if count_[-1] == dic[i]:
                    count_.pop(-1)
                    continue
                return False
            return False
        if count_:
            return False
        return True

a = Solution()
print(a.isValid("{}"))
