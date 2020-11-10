class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if obstacleGrid[-1][-1] != 1 and obstacleGrid[0][0] != 1:
            length = len(obstacleGrid[0])
            height = len(obstacleGrid)
            for i in range(length):
                for j in range(height):
                    if obstacleGrid[j][i]:
                        obstacleGrid[j][i] = 'B'
            print(obstacleGrid)
            for i in range(length):
                if obstacleGrid[0][i] == 'B':
                    break
                obstacleGrid[0][i] = 1

            for j in range(height):
                if obstacleGrid[j][0] == 'B' :
                    break
                obstacleGrid[j][0] = 1
            [print(i) for i in obstacleGrid]
            print()

            for i in range(1, length):
                for j in range(1, height):
                    if obstacleGrid[j][i] != 'B':
                        obstacleGrid[j][i] = (obstacleGrid[j - 1][i] if obstacleGrid[j - 1][i] != 'B' else 0) + (
                            obstacleGrid[j][i - 1] if obstacleGrid[j][i - 1] != 'B' else 0)
            [print(i) for i in obstacleGrid]
            return obstacleGrid[-1][-1]
        print('a')
        return 0


s = Solution()
print(s.uniquePathsWithObstacles([[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))
