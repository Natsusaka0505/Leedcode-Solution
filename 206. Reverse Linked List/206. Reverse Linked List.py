from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: 31 ms (94.39%), Space: 17.72 MB (94.38%)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            # next = curr.next
            # curr.next = prev
            # prev = curr

            # curr = next

        return prev


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
head = sol.reverseList(head)


while head:
    print(head.val, end=", ")
    head = head.next
