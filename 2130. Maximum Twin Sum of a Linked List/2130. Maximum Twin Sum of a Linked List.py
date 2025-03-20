from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: 347 ms (87.58%), Space: 45.43 MB (46.72%)
class Solution1:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        cnt = 0
        while curr:
            curr = curr.next
            cnt += 1

        curr = head
        target = cnt / 2
        # print(f"target: {target}")
        cnt = 0
        stack1 = []
        stack2 = []

        while curr and cnt != target:
            stack1.append(curr.val)
            print(f"{curr.val}")
            curr = curr.next
            cnt += 1

        while curr and cnt != target * 2:
            stack2.append(stack1.pop() + curr.val)
            curr = curr.next
            cnt += 1

        return max(stack2)


# Time: 312 ms (99.12%), Space: 38.33 MB (83.66%)
class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        maxVal = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal


#  Testing
head = [5, 4, 2, 1]

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

sol = Solution2()
print(sol.pairSum(head))

# while head:
#     print(head.val, end=", ")
#     head = head.next
