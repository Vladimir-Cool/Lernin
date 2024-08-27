from typing import Optional, List


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def create_List_Node(row_list: List[int]):
    head = ListNode(0)
    current = head

    for el in row_list:
        new_node = ListNode(el)
        current.next = new_node
        current = new_node
    return head.next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    temp_head = ListNode(0, head)
    count = 0
    current: ListNode = head

    while current:
        count += 1
        current = current.next

    current1 = temp_head
    for i in range(count - n):
        current1 = current1.next
    print(temp_head.val)
    current1.next = current1.next.next

    return temp_head.next


def removeNthFromEnd2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    temp_head = ListNode(0, head)
    current: ListNode = temp_head

    while n > 0 and head:
        head = head.next
        n -= 1

    while head is not None:
        head = head.next
        current = current.next

    current.next = current.next.next

    return temp_head.next


test = [1, 2, 3, 4, 5]
test_lnode = create_List_Node(test)
print(removeNthFromEnd(test_lnode, 4))
print(removeNthFromEnd2(test_lnode, 4))
