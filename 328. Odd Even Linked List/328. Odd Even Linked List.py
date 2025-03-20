from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: 33 ms (95.31%), Space: 18.50 MB (99.87%)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head


#  Testing
head = [1, 3, 4, 7, 1, 2, 6]

dummy = ListNode()
cur = dummy

for val in head:
    cur.next = ListNode(val)
    cur = cur.next


head = dummy.next


while head:
    print(head.val, end=", ")
    head = head.next
print("")

head = dummy.next

sol = Solution()
sol.oddEvenList(head)

while head:
    print(head.val, end=", ")
    head = head.next
