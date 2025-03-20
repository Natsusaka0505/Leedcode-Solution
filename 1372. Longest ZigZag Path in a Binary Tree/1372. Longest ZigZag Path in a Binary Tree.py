from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: 168 ms (95.79%), Space: 31.15 MB (60.01%)
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.travel(root.left, True, 0), self.travel(root.right, False, 0))

    def travel(self, node, isLeft, depth):
        if not node:
            return depth

        if isLeft:
            depth = max(
                depth,
                self.travel(node.right, False, depth + 1),
                self.travel(node.left, True, 0),
            )
        else:
            depth = max(
                depth,
                self.travel(node.left, True, depth + 1),
                self.travel(node.right, False, 0),
            )

        return depth
