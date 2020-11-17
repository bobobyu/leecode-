from Link import *


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        elif not head.next:
            return head
        odd: ListNode = head.next
        odd_head = odd
        even: ListNode = head
        even_head = even
        head = odd.next
        flag: bool = False
        while head:
            if flag:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            flag = not flag
        even.next = odd_head
        odd.next = None
        return even_head

l = Link([2,1,3,5,6,4,7])
s= Solution()
x = s.oddEvenList(l.head_node)
l.show(x)
