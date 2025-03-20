from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time: 39 ms (98.18%), Space: 21.11 MB (72.37%)
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None
        if not root.left and not root.right:
            return root

        return self.travel(root, p, q)

    def travel(self, node, p, q):
        if not node:
            return None

        if node == q or node == p:
            return node

        left = self.travel(node.left, p, q)
        right = self.travel(node.right, p, q)

        if left and right:
            return node

        return left or right
