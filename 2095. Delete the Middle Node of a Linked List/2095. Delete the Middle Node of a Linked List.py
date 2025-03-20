# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: 567 ms (99.61%), Space: 50.25 MB (99.55%)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = fast = head
        prev = None

        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

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
sol.deleteMiddle(head)

while head:
    print(head.val, end=", ")
    head = head.next
