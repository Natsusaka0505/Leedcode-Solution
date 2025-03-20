# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: 34 ms (93.95%), Space: 18.50 MB (99.87%)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        cnt = self.visitNode(root)

    def visitNode(self, node: TreeNode) -> int:
        cnt = 0
        if not node:
            return 0

        cnt += 1

        return self.visitNode(node.left) + self.visitNode(node.right)
