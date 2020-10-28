from Link import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node: ListNode = ListNode()
        if not l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if l1 and not l2:
            return l1
        head = new_node

        while l1 and l2:
            l1_value = l1.val
            l2_value = l2.val
            # print(l1_value, l2_value)
            if l1_value <= l2_value:
                new_node.val = l1_value
                l1 = l1.next
            else:
                new_node.val = l2_value
                l2 = l2.next
            if l1 and l2:
                new_node.next = ListNode()
                new_node = new_node.next
            else:
                break
            # print(new_node.val)
        if l1 and not l2:
            new_node.next = l1
        elif l2 and not l1:
            new_node.next = l2
        return head


a = Link([8])
b = Link([2, 6])
s = Solution()
h = s.mergeTwoLists(a.head_node, b.head_node)
a.show(h)
