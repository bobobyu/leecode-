from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        merge_point: int = 0
        while merge_point < len(points) - 1:
            pre_coordinate = points[merge_point]
            next_coordinate = points[merge_point + 1]
            if pre_coordinate[-1] >= next_coordinate[0]:
                points[merge_point] = [max(pre_coordinate[0], next_coordinate[0]),
                                       min(pre_coordinate[-1], next_coordinate[-1])]
                points.pop(merge_point + 1)
            else:
                merge_point += 1
        return len(points)


s = Solution()
s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
