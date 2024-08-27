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


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    new_list_node = ListNode(0)
    current = new_list_node

    while list1 or list2:
        if list1 and list2 and list1.val <= list2.val:
            current.next = list1
            current = list1
            list1 = list1.next
        elif not list1 and list2:
            current.next = list2
            current = list2
            list2 = list2.next
        elif not list2 and list1:
            current.next = list1
            current = list1
            list1 = list1.next
        else:
            current.next = list2
            current = list2
            list2 = list2.next
        print(current.val)
    return new_list_node.next


def mergeTwoLists2(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    current = new_lnode = ListNode(0)

    while list1 and list2:
        if list1.val <= list2.val:
            current.next, list1 = list1, list1.next
        else:
            current.next, list2 = list2, list2.next
        current = current.next

    if list1 or list2:
        current.next = list1 if list1 else list2

    return new_lnode.next


test1 = [1, 2, 4]
test2 = [1, 3, 4]

test_lnode1 = create_List_Node(test1)
test_lnode2 = create_List_Node(test2)

result = mergeTwoLists(test_lnode1, test_lnode2)
result2 = mergeTwoLists2(test_lnode1, test_lnode2)
