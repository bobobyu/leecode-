from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pro_s: List[str] = [i.lower() for i in s if i.isalpha() or i.isalnum()]
        # print(''.join(pro_s), ''.join(pro_s[::-1]))
        return ''.join(pro_s) == ''.join(pro_s[::-1])


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
