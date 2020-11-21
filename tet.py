# from Link import *
# from typing import List
#
# a = Link([1,4])
# b = Link([2,2,3])
#
# left_link = a.head_node
# right_link = b.head_node
# right_empty: ListNode = ListNode()
# left_empty: ListNode = ListNode()
# right_empty.next = b.head_node
# left_empty.next = a.head_node
#
# pre_left: ListNode = left_empty
#
#
# # def insert_node(left: ListNode, right: ListNode, front: bool, pre_left_: ListNode = None,
# #                 ) -> List[ListNode]:
# #     a.show(left_empty.next)
# #     print(end=',')
# #     a.show(right_empty)
# #     print()
# #     if front:
# #         left_tmp: ListNode = left.next
# #         if not left_tmp:
# #             left.next = right
# #             right_empty.next = right.next
# #             return [right, left, right_empty.next]
# #         return [left_tmp, left, right]
# #     else:
# #         right_empty.next = right.next
# #         pre_left_.next = right
# #         right.next = left
# #         right_ = right_empty.next
# #         return [left.next, left, right_]
#
#
# while right_empty.next:
#     # a.show(left_empty)
#     # a.show(right_empty)
#     if left_link.val <= right_link.val:
#         if not left_link.next:
#             left_link.next = right_link
#             right_empty.next = None
#             break
#         else:
#             left_link = left_link.next
#             pre_left = left_link
#     else:
#         right_empty.next = right_link.next
#
#         pre_left.next = right_link
#         right_link.next = left_link
#
#         pre_left = right_link
#         right_link = right_empty.next
#
#
# a.show(left_empty.next)
#

# import pandas as pd
#
# row_index = ['index', 'name', 'ID']
# total_name_sheet = pd.read_excel('C:\\Users\\Administrator\\Desktop\\total.xlsx', sheet_name=1, names=row_index)
# total_names = set(total_name_sheet['name'])
#
# had_studied = pd.read_excel('C:\\Users\\Administrator\\Desktop\\第十季第六期（特辑）周六各班级完成情况.xlsx', sheet_name='计算机专业2018级5班')
# studied_names = set(had_studied['姓名'])
# print(total_names - studied_names)