class Solution:
    def exist(self, board: list, word: str) -> bool:
        row_num: int = len(board)
        col_num: int = len(board[0])
        s_length: int = len(word)
        self.b = False
        self.flag = False

        def search(i: int, j: int, layer: int = 0, invalid: list = []):
            print(layer, (i,j), s_length)
            if layer == s_length:
                self.b = True
                self.flag = True
                return
            elif not self.flag:
                if 0 < i:
                    if word[layer] == board[i - 1][j] and [i - 1, j] not in invalid:
                        print(board[i - 1][j], (i - 1, j), '\n')
                        search(i - 1, j, layer + 1, invalid + [[i - 1, j]])
                if i < row_num - 1:
                    if word[layer] == board[i + 1][j] and [i + 1, j] not in invalid:
                        print(board[i + 1][j], (i + 1, j), '\n')
                        search(i + 1, j, layer + 1, invalid + [[i + 1, j]])
                if 0 < j:
                    if word[layer] == board[i][j - 1] and [i, j - 1] not in invalid:
                        print(board[i][j - 1], (i, j - 1), '\n')
                        search(i, j - 1, layer + 1, invalid + [[i, j - 1]])
                if j < col_num - 1:
                    if word[layer] == board[i][j + 1] and [i, j + 1] not in invalid:
                        print(board[i][j + 1], (i, j + 1), '\n')
                        search(i, j + 1, layer + 1, invalid + [[i, j + 1]])

        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] == word[0]:
                    search(i, j, layer=1, invalid=[[i, j]])
                    if self.b:
                        return True
        return False


s = Solution()
print(s.exist(board=
    [["a", "a", "b", "b"],
     ["a", "a", "b", "b"]]
, word='baa'))
