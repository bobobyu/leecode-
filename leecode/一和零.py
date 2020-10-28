class Solution:

    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        matrix = [[0 for i in range(m+1)] for j in range(n+1)]
        for item in strs:
            zero_consume = item.count('0')
            one_consume = item.count('1')
            for one_count in range(n, one_consume-1, -1):
                for zero_count in range(m, zero_consume-1, -1):
                    matrix[one_count][zero_count] = max(matrix[one_count-one_consume][zero_count-zero_consume]+1, matrix[one_count][zero_count])
        return matrix[n][m]
a = Solution()
print(a.findMaxForm(["10","0001","111001","1","0"]
                    , 5, 3))
