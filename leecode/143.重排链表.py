from Link import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            head_root = head
            root_list = []
            while head:
                root_list.append(head)
                head = head.next
            if len(root_list) >1:
                head_list = root_list[1:len(root_list) // 2 + 1]
                end_list = root_list[len(root_list) // 2 + 1:][::-1]
                # [print(i.val,end=' ') for i in head_list]
                # print('\n')
                # [print(i.val, end=' ') for i in end_list]
                # print()
                mer_list = []
                for i in zip(head_list, end_list):
                    mer_list += [i[1], i[0]]
                if len(head_list) > len(end_list):
                    mer_list.append(head_list[-1])
                head_root.next = mer_list[0]
                for i in range(len(mer_list) - 1):
                    mer_list[i].next = mer_list[i + 1]
                mer_list[-1].next = None



s = Solution()
l = Link([1])
s.reorderList(l.head_node)
l.show(l.head_node)
