from Link import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list: list = []
        empty_node = ListNode()
        empty_node.next = head
        head = empty_node
        head_node = head
        while head:
            node_list.append(head)
            head = head.next
        if len(node_list)>1:
            node_list[-n - 1].next = node_list[-n + 1] if n > 1 else None
            del node_list[-n]
            return head_node.next
        return None

s = Solution()
a = Link([1,2])
x = s.removeNthFromEnd(a.head_node, 2)
a.show(x)
