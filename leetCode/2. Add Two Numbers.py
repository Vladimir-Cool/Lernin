
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l = [1, 2]

n1 = ListNode(1, 2)
n2 = ListNode(2)

print(n1.val)
print(n1.next)
print(n2.val)
print(n2.next)