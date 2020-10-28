class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s:
            s = s.split(' ')
            s = [i for i in  s if i]
            return len(s[-1]) if s else 0
        else:
            return 0


s = Solution()
print(s.lengthOfLastWord("  "))
