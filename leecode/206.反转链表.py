# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Link import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        root_list = []
        while head:
            root_list.append(head)
            head = head.next
        if root_list:
            root_list.reverse()
            head_root = root_list[0]
            for i in range(len(root_list)-1):
                root_list[i].next = root_list[i+1]
            root_list[-1].next = None
            return head_root

s = Solution()
L = Link([1,2,3,4,5])
x = s.reverseList(None)
L.show(x)