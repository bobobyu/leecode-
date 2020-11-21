from Link import *
from time import sleep

def merge(main_head, vice_head) -> ListNode:
    main_empty: ListNode = ListNode()
    vice_empty: ListNode = ListNode()
    main_empty.next = main_head
    vice_empty.next = vice_head
    pre_node: ListNode = main_empty
    while vice_empty.next:
        a.show(main_empty)
        print()
        b.show(vice_empty)
        print('\n\n')
        # sleep(5)
        if main_head.val <= vice_head.val:
            pre_node = pre_node.next
            main_head = main_head.next
            continue
        vice_empty.next = vice_head.next

        pre_node.next = vice_head
        vice_head.next = main_head

        main_head = vice_head
        vice_head = vice_empty.next
    return main_empty.next

a = Link([1,5,6])
b = Link([1,3,7])
a.show(merge(a.head_node, b.head_node))

