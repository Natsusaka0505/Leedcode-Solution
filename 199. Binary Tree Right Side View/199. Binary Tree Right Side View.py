from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: 38 ms (51.88%), Space: 16.52 MB (71.89%)
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        queue = deque([root])
        res = []

        while queue:
            rightMost = None
            n = len(queue)
            for i in range(n):
                node = queue.popleft()

                if node:
                    rightMost = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightMost:
                res.append(rightMost.val)

        return res


# Time: 23 ms (99.48%), Space: 16.54 MB (71.89%)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        rightside = []

        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside
