from Link import *


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        lists = [i for i in lists if i]
        if not lists:
            return None
        current_node = ListNode()
        head_node: ListNode = current_node
        while True:
            alternative_list = [i.val for i in lists]
            min_num = min(alternative_list)
            min_num_index = alternative_list.index(min_num)
            current_node.val = min_num
            lists[min_num_index] = lists[min_num_index].next
            print(alternative_list)
            if not lists[min_num_index]:
                lists.pop(min_num_index)
            if [i for i in lists if i]:
                next_node: ListNode = ListNode()
                current_node.next = next_node
                current_node = next_node
            else:
                break
        return head_node



s = Solution()
a1 = Link([1, 4, 5])
a2 = Link([1,3,4])
a3 = Link([2,6])
print(a1)
h = s.mergeKLists([None])
a1.show(h)
