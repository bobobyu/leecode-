class Solution:
    def islandPerimeter(self, grid: list) -> int:
        length: int = len(grid[0])
        width: int = len(grid)
        C: int = 0
        print(grid[3][0])
        for x in range(length):
            for y in range(width):
                print(x, y, grid[y][x])
                left = x == 0 or not grid[y][x - 1]
                print(left, 'l', end=' ')
                right = x == length - 1 or not grid[y][x + 1]
                print(right, 'r', end=' ')
                top = y == 0 or not grid[y - 1][x]
                print(top, 't', end=' ')
                button = y == width - 1 or not grid[y + 1][x]
                print(button, 'b', end=' ->')
                print(grid[y][x] and left + right + top + button, end=' ')
                C += grid[y][x] and sum([
                    ((x == 0) or not grid[y][x - 1]),
                    ((x == length - 1) or not grid[y][x + 1]),
                    ((y == 0) or not grid[y - 1][x]),
                    ((y == width - 1) or not grid[y + 1][x]),
                ])

                print(grid[y][x] ,[
                    ((x == 0) or not grid[y][x - 1]),
                    ((x == length - 1) or not grid[y][x + 1]),
                    ((y == 0) or not grid[y - 1][x]),
                    ((y == width - 1) or not grid[y + 1][x]),
                ],'C->', C)
        return C


s = Solution()
print(s.islandPerimeter(
    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]))
