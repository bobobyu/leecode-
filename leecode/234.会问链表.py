from Link import *


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head:
            node_list: list = []
            while head:
                node_list.append(head.val)
                head = head.next
            end_point = len(node_list) -1
            for i in range(len(node_list)//2):
                if node_list[i] != node_list[end_point]:
                    return False
                end_point -= 1
            return True
        return True
S = Solution()
l = Link([1])
print(S.isPalindrome(l.head_node))