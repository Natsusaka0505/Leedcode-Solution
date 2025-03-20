# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: 45 ms (97.37%), Space: 18.26 MB (88.21%)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root

        def travel(node, val):
            nonlocal res
            if node.val == val:
                res = node
                return
            if node.left:
                travel(node.left, val)
            if node.right:
                travel(node.right, val)

        res = None
        travel(root, val)

        return res


# Time: 53 ms (73.88%), Space: 18.34 MB (49.40%)
class Solution2:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        def travel(node, val):
            if not node:
                return None

            if node.val == val:
                return node

            result = travel(node.left, val) or travel(node.right, val)
            return result

        return travel(root, val)


# Time: 34 ms (99.93%), Space: 18.42 MB (30.04%)
class Solution3:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)

        else:
            return self.searchBST(root.left, val)
