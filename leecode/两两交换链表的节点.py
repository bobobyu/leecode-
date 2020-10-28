from Link import *


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            head_node: ListNode = head
            end_node: ListNode = head
            while True:
                if end_node.next:
                    end_node = end_node.next
                else:
                    break
            end_node.next = ListNode(-1)
            head_empty_node: ListNode = ListNode(-1)
            head_empty_node.next = head_node

            def dp(node: ListNode, pre_node: ListNode):
                if node.next and node.next.val>-1:
                    print(node.val, node.next.val)
                    first_node: ListNode = node
                    second_node: ListNode = node.next
                    pre_node.next = second_node
                    first_node.next = second_node.next
                    second_node.next = first_node
                    if first_node.next and first_node.next.val>-1:
                        return dp(node=first_node.next, pre_node=first_node)
                    else:
                        return first_node
                else:
                    return node

            end_node = dp(node=head_node, pre_node=head_empty_node)
            end_node.next = None
            return head_empty_node.next
        return head

s= Solution()
a =Link([4,0,6,2,8])
a.show(s.swapPairs(a.head_node))