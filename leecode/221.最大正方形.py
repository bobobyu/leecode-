class Solution:
    def maximalSquare(self, matrix: list) -> int:
        if not matrix:
            return 0
        col_length: int = len(matrix[0])
        row_length: int = len(matrix)
        max_area: int = 0
        for i in range(row_length):
            if row_length - i <= max_area:
                break
            for j in range(col_length):
                if col_length - j <= max_area:
                    break
                if matrix[i][j] == '1':
                    diagonal = 1
                    while diagonal < min(row_length - i, col_length - j) and matrix[i + diagonal][j + diagonal] == '1':
                        count_point = 1
                        while count_point <= diagonal and matrix[i + diagonal - count_point][j + diagonal] == '1' and \
                                matrix[i + diagonal][j + diagonal - count_point] == '1':
                            count_point += 1
                        if count_point - 1 != diagonal:
                            max_area = max(max_area, diagonal)
                            break
                        diagonal += 1
                    max_area = max(max_area, diagonal)
        return max_area**2


s = Solution()
print(s.maximalSquare([["1", "0", "1", "0", "0"],
                       ["1", "0", "1", "1", "1"],
                       ["1", "1", "1", "1", "1"],
                       ["1", "0", "0", "1", "0"]]))
