class Solution:
    def generateParenthesis(self, n: int) -> list:
        result: list = []

        def dp(l: int = 0, r: int = 0, curr_string: str = '', n: int = n) -> None:
            print(curr_string)
            l == r == n and result.append(curr_string)
            l < n and dp(l + 1, r, curr_string + '(')
            r < l and dp(l, r + 1, curr_string + ')')

        dp()
        return result


s = Solution()
print(s.generateParenthesis(3))
