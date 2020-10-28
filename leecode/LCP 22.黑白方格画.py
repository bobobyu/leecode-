class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k >= n:
            if k == n*n:
                return 1
            count_ = 0
            fac_dict: dict = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}
            result_list: list = []
            for i in range(n + 1):
                for j in range(n + 1):
                    if n * (i + j) - i * j == k:
                        result_list.append([i, j])

            # def rec(n: int) -> int:
            #     if n == 1 or n == 0:
            #         return 1
            #     return n * rec(n - 1)
            for i in result_list:
                print(i)
                if i[0]:
                    row_count = fac_dict[n] / (fac_dict[i[0]] * fac_dict[n - i[0]])
                else:
                    row_count = 1
                if i[1]:
                    col_count = fac_dict[n] / (fac_dict[i[1]] * fac_dict[n - i[1]])
                else:
                    col_count = 1
                count_ += row_count * col_count
            return int(count_)
        return 0 if k else 1


s = Solution()
print(s.paintingPlan(1, 0))
