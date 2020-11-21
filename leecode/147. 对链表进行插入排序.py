from Link import *

class Solution:
    def __init__(self):
        self.empty_node: ListNode = ListNode(-float('inf'))

    def insertionSortList(self, head: ListNode) -> ListNode:
        self.empty_node.next = head
        sort_end: ListNode = head
        next_node: ListNode = self.empty_node.next

        def insert_node_to_sort_limit(sort_end_: ListNode, insert_node: ListNode) -> ListNode:
            if insert_node != sort_end:
                pre_node_ = self.empty_node
                current_node = pre_node_.next
                while pre_node_ != sort_end_:
                    if current_node.val >= insert_node.val:
                        pre_node_.next = insert_node
                        insert_node.next = current_node
                        return sort_end_
                    pre_node_ = current_node
                    current_node = current_node.next
                return insert_node
            return sort_end

        while next_node:
            if sort_end.val > next_node.val:
                sort_end.next = next_node.next
                # h.show(self.empty_node)
                # print(',',sort_end.val)
                sort_end = insert_node_to_sort_limit(sort_end_=sort_end, insert_node=next_node)
                # print()
                next_node = sort_end.next
            else:
                sort_end = next_node
                next_node = next_node.next


        # print(self.empty_node.next.val)
        return self.empty_node.next
s = Solution()
h = Link([4])
x = s.insertionSortList(h.head_node)
h.show(x)