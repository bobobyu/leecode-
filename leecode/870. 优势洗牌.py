from typing import List
from collections import defaultdict


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        b_index: defaultdict = defaultdict(list)
        for i, j in enumerate(B):
            b_index[j].append(i)

        A.sort(reverse=True)
        b_ = sorted(B, reverse=True)

        b_point: int = 0
        # print(b_, A)
        # print(b_index)

        while b_point < len(B):
            # print(A, b_[b_point])
            if A[0] > b_[b_point]:

                index_ = b_index[b_[b_point]].pop()
                B[index_] = A.pop(0)
                # print(index_, [b_[b_point]], B)

            b_point += 1
            # print()
        xx: list = [i for i in b_index.values()]
        unused_index = []
        for i in xx:
            if i:
                unused_index += i
        # print(B)
        for i, j in zip(unused_index, A):
            B[i] = j
        return B

s = Solution()
print(s.advantageCount(A = [2,7,11,15], B = [1,10,4,11]))
A = [12, 24, 8, 32], [32, 24, 12, 8]
B = [13, 25, 32, 11], [32, 25, 13, 11]
C = [24, 32, 8, 12]
