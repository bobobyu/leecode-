class Solution:
    def solveNQueens(self, n: int) -> list:
        self.res: list = []

        def check(new_strategy: int, strategy: list):
            layer = len(strategy)
            for i, j in enumerate(strategy):
                if abs(layer - i) == abs(new_strategy - j):
                    return False
            return True

        def dp(board: list,layer: int = 0):
            if layer == n:
                draw_board = [['.' for _ in range(n)] for __ in range(n)]
                for i, j in enumerate(board):
                    draw_board[i][j] = 'Q'
                draw_board = [''.join(i) for i in draw_board]
                self.res.append(draw_board)
            for i in range(n):
                if i not in board and check(i, board):
                    dp(board + [i], layer=layer + 1)
        dp(board=[])
        return self.res

s = Solution()
print(s.solveNQueens(4))