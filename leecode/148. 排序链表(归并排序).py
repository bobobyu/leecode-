from Link import *
from typing import List


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge_sort(head_node: ListNode) -> ListNode:
            if not head_node.next:
                return head_node

            fast_point: ListNode = head_node
            slow_point: ListNode = head_node
            while True:
                fast_point = fast_point.next
                if fast_point and fast_point.next:
                    fast_point = fast_point.next
                else:
                    break
                slow_point = slow_point.next

            # a.show(head_node)
            vice_node = slow_point.next
            slow_point.next = None
            # vice_node.pre = None

            # a.show(head_node)
            # a.show(vice_node)
            # print(fast_point.val)
            # print(vice_node.val)
            # print(vice_node.val)
            # print('----')
            # sleep(0.5)

            main_head: ListNode = merge_sort(head_node=head_node)
            vice_head: ListNode = merge_sort(head_node=vice_node)

            # a.show(main_head)
            # a.show(vice_node)
            # print('--')
            # print()

            main_empty: ListNode = ListNode()
            vice_empty: ListNode = ListNode()
            main_empty.next = main_head
            main_head.pre = main_empty
            vice_empty.next = vice_head
            vice_head.pre = vice_empty

            while vice_empty.next:

                if vice_head.val <= main_head.val:

                    vice_empty.next = vice_head.next
                    if vice_head.next:
                        vice_head.next.pre = vice_empty
                    vice_head.pre = None
                    vice_head.next = None

                    main_head.pre.next = vice_head
                    vice_head.pre = main_head.pre

                    vice_head.next = main_head
                    main_head.pre = vice_head

                    vice_head = vice_empty.next
                elif vice_head.val > main_head.val and not main_head.next:

                    vice_empty.next = vice_head.next
                    if vice_head.next:
                        vice_head.next.pre = vice_empty
                    vice_head.pre = None
                    vice_head.next = None

                    vice_head.pre = main_head
                    main_head.next = vice_head

                    main_head = vice_head
                    vice_head = vice_empty.next
                else:
                    main_head = main_head.next
            # a.show(main_empty.next)
            # print('<>')
            return main_empty.next
        return merge_sort(head_node=head)

a = Link([2,1,3,4,5,1234,2345,12,34,])
S = Solution()
x = S.sortList(a.head_node)
a.show(x)