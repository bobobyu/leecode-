from Link import *
from time import sleep


def merge(main_head, vice_head) -> ListNode:
    main_empty: ListNode = ListNode()
    vice_empty: ListNode = ListNode()
    main_empty.next = main_head
    vice_empty.next = vice_head
    pre_node: ListNode = main_empty
    while vice_empty.next:
        if main_head.val <= vice_head.val and main_head.next:
            pre_node = pre_node.next
            main_head = main_head.next
            continue
        if main_head.val > vice_head.val:
            vice_empty.next = vice_head.next

            pre_node.next = vice_head
            vice_head.next = main_head

            pre_node = vice_head
            vice_head = vice_empty.next
        else:
            vice_empty.next = None
            main_head.next = vice_head

    return main_empty.next


a = Link([1, 5, 6, 8])
b = Link([4, 3, 7])
a.show(merge(a.head_node, b.head_node))
