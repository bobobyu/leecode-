from Link import *



class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        empty_node = ListNode(-1)
        if head and head.next:
            f_point: ListNode = head
            s_point: ListNode = head
            ss_point: ListNode = head
            cycle_start_position: int = 0

            for _ in range(2):
                f_point = f_point.next
            s_point = s_point.next

            while f_point != s_point and f_point:
                for _ in range(2):
                    if f_point.next:
                        f_point = f_point.next
                    else:
                        return empty_node
                s_point = s_point.next
            if f_point:
                while s_point != ss_point:
                    cycle_start_position += 1
                    ss_point = ss_point.next
                    s_point = s_point.next
                    cycle_start_position += 1
                return ss_point
            return empty_node
        return empty_node
a = Link([1])
# a.end_node.next = a.head_node

s = Solution()
print(s.detectCycle(a.head_node).val)
