class Solution:
    def reverseString(self, s: list) -> None:
        start_index: int = 0
        end_index: int = len(s) - 1
        while start_index < end_index:
            s[start_index], s[end_index] = s[end_index], s[start_index]
            start_index += 1
            end_index -= 1

a = Solution()
s = [1,2,3]
a.reverseString(s)
print(s)
