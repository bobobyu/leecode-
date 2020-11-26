class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        center_distance: float = pow(
            pow(x_center - ((x1 + x2) / 2), 2) + pow(y_center - ((y1 + y2) / 2), 2),
            0.5)
        # diagonal_line: float = pow(pow(x1 - rectangle_center[0], 2) + pow(y1 - rectangle_center[1], 2),
        #                            0.5)
        print(center_distance, abs(x1 - x2) / 2 + radius)
        if center_distance <= (abs(x1 - x2) / 2) + radius:
            return True

        dis_ = lambda x1, y1: pow(pow(x1 - x_center, 2) + pow(y1 - y_center, 2),
                                  0.5)
        for i in [[x1, y1], [x2, y2], [x1, y2], [x2, y1]]:
            print(dis_(i[0], i[1]))
            if dis_(i[0], i[1]) <= radius:
                return True
        return False


s = Solution()
print(s.checkOverlap(10,
                     10,
                     1,
                     0,
                     0,
                     100,
                     100))
'''
0,0
100,100
0,100
100,0
'''
