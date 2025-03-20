# Definition for a binary tree node.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: 109 ms (99.35%), Space: 30.90 MB (95.75%)
class Solution:
    def __init__(self, cnt=0):
        self.cnt = cnt

    def travel(self, node, maxNum) -> int:
        if not node:
            return 0

        if node.val >= maxNum:
            maxNum = node.val
            self.cnt += 1

        self.travel(node.left, maxNum)
        self.travel(node.right, maxNum)

        return

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        self.travel(root, -sys.maxsize - 1)

        return self.cnt
