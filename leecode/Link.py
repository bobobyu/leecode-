# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next

class Link:
    def __init__(self, list_:list):
        self.head_node = ListNode(list_[0])
        pre_node = self.head_node
        for i in list_[1:]:
            current_node = ListNode(val=i)
            pre_node.next = current_node
            pre_node = current_node
        self.end_node = pre_node
    def show(self, current):
        if current:
            print(current.val,sep=' ', end=' ')
            self.show(current.next)
