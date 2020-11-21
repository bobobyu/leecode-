from Link import *
from typing import List


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge_sort(head_node: ListNode) -> ListNode:
            if not head_node.next:
                return head_node
            fast_point: ListNode = head
            slow_point: ListNode = head
            while fast_point:
                fast_point = fast_point.next.next
                slow_point = slow_point.next

            left_link: ListNode = merge_sort(head_node=head_node)
            right_link: ListNode = merge_sort(head_node=slow_point)

            right_empty: ListNode = ListNode()
            left_empty: ListNode = ListNode()
            right_empty.next = right_link
            left_empty.next = left_link
            pre_left: ListNode = left_empty

            while right_empty.next:
                if left_link.val <= right_link.val:
                    if not left_link.next:
                        left_link.next = right_link
                        right_empty.next = None
                        break
                    else:
                        left_link = left_link.next
                        pre_left = left_link
                else:
                    right_empty.next = right_link.next

                    pre_left.next = right_link
                    right_link.next = left_link

                    pre_left = right_link
                    right_link = right_empty.next
            return left_empty.next
