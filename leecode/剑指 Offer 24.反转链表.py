from Link import *
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            Link_list:list = []
            while head:
                Link_list.append(head)
                head = head.next
            Link_list.reverse()

            for i, j in enumerate(Link_list):
                Link_list[i].next = Link_list[min(i+1, len(Link_list) - 1)]
            Link_list[-1].next = None
            return Link_list[0]
l = Link([1,2,3,4,5])
s = Solution()
h = s.reverseList(l.head_node)
l.show(h)