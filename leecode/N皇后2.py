class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result_count: int = 0
        board_size: int = n

        def check_valid(sol: list):
            for i in range(board_size):
                for j in range(i + 1, board_size):
                    if abs(i - j) == abs(sol[i] - sol[j]):
                        return None
            self.result_count += 1
        def dp(sol: list, layer=n):
            if layer == 0:
                check_valid(sol)
            for i in range(board_size):
                if i not in sol:
                    dp(sol=sol+[i], layer=layer - 1)
        dp(sol=[])
        return self.result_count

s = Solution()
print(s.totalNQueens(8))