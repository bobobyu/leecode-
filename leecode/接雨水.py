# class Solution:
#     def trap(self, height: list) -> int:
#
#         left_bound = 0
#         right_bound = 1
#         tem_volume: list = []
#         height_length: int = len(height)
#         volume: int = 0
#         while height_length >= 3 and right_bound < height_length:
#             while right_bound < height_length and height[left_bound] > height[right_bound]:
#                 tem_volume.append(right_bound)
#                 right_bound += 1
#             if right_bound < height_length or height[right_bound - 1] >= height[left_bound]:
#                 for i in tem_volume:
#                     volume += height[left_bound] - height[i]
#             else:
#                 if len(tem_volume) >= 3:
#                     left_bound = 0
#                     right_bound = 1
#                     height = [height[i] for i in tem_volume]
#                     height_length = len(height)
#                     tem_volume.clear()
#                     # print(height,height_length)
#                     while right_bound < height_length:
#                         while right_bound < height_length and height[left_bound] > height[right_bound]:
#                             tem_volume.append(right_bound)
#                             right_bound += 1
#                         # print(left_bound, right_bound, tem_volume)
#                         if right_bound < height_length or height[right_bound - 1] >= height[left_bound]:
#                             for i in tem_volume:
#                                 volume += height[left_bound] - height[i]
#                         left_bound = right_bound
#                         right_bound += 1
#                         tem_volume.clear()
#                 return volume
#
#             tem_volume.clear()
#             # print()
#             left_bound = right_bound
#             right_bound += 1
#         return volume
#
#
# s = Solution()
# print(s.trap(
#     [0,0,1,0,3,1,0,1,0]))

class Solution:
    def trap(self, height: list) -> int:
        if len(height) > 2:
            left_bound: int = 0
            right_bound: int = 1
            s_length: int = len(height)
            volume: int = 0

            while right_bound < s_length:
                if height[right_bound] <= height[left_bound]:
                    volume += height[left_bound] - height[right_bound]
                else:
                    left_bound = right_bound
                print(left_bound, right_bound)
                right_bound += 1
            return volume
        else:
            return 0


s = Solution()
print(s.trap([1, 3, 1, 3, 1, 0, 1]))
