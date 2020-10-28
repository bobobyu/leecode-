from Link import *


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            fast_point: ListNode = head.next
            slow_point: ListNode = head
            while fast_point and slow_point != fast_point:
                for _ in range(2):
                    if fast_point.next:
                        fast_point = fast_point.next
                    else:
                        return False
                slow_point = slow_point.next
            return True if fast_point else False
        return False

    def dp(self, fast: ListNode, slow: ListNode):
        if fast and slow:
            next_ = fast.next
            next__ = next_.next
            if next__ and next_:
                return fast == slow or self.dp(next__, slow.next)
            else:
                return False
        return False

    def DP(self, head: ListNode):
        if head:
            return self.dp(head.next, head)
        return False


a = Link([1, 2, 3, 4])
a.end_node.next = a.head_node
s = Solution()
print(s.DP(a.head_node))
