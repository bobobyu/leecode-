from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        target_coordinate: List[int] = [r0, c0]
        other_coordinate: List[List[int]] = [[r, c] for r in range(R) for c in range(C)]
        return sorted(other_coordinate, key=lambda x:abs(target_coordinate[0]-x[0])+abs(target_coordinate[1]-x[1]))