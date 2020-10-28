class Solution:
    def solveNQueens(self, n: int) -> list:
        self.result_count: list = []
        board_size: int = n

        def check_valid(sol: list):
            for i in range(board_size):
                for j in range(i + 1, board_size):
                    if abs(i - j) == abs(sol[i] - sol[j]):
                        return
            visual_board = ['' for _ in range(n)]
            for i, j in enumerate(sol):
                for x in range(n):
                    visual_board[i] += '.' if x != j else 'Q'
            self.result_count.append(visual_board)
        def dp(sol: list, layer=n):
            if layer == 0:
                check_valid(sol)
            for i in range(board_size):
                if i not in sol:
                    dp(sol=sol + [i], layer=layer - 1)

        dp(sol=[])
        return self.result_count

s = Solution()
print(s.solveNQueens(4))