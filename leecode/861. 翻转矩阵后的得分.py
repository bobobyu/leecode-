from typing import *


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i, j in enumerate(A):
            if j[0] == 0:
                j[1:] = [not i for i in j[1:]]
        A_: List[Tuple[int]] = [i for i in zip(*A)]
        rows: int = len(A)
        cols: int = len(A[0])
        score_: int = pow(2, cols - 1) * rows
        for i, j in enumerate(A_[1:]):
            # print(pow(2, cols - i - 2) * zero_count if (zero_count := j.count(0)) > (
            #     one_count := rows - zero_count) else pow(2, cols - i - 2) * one_count)
            score_ += pow(2, cols - i - 2) * zero_count if (zero_count := j.count(0)) > (
                one_count := rows - zero_count) else pow(2, cols - i - 2) * one_count
        # print(score_)
        return score_


s = Solution()
s.matrixScore([[0, 0, 1, 1],
               [1, 0, 1, 0],
               [1, 1, 0, 0]])
