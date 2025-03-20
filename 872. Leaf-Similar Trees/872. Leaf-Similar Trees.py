# Definition for a binary tree node.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: 27 ms (97.36%), Space: 16.61 MB (91.02%)
class Solution:
    def travel(self, node, ls):
        if not node:
            return

        if not node.left and not node.right:
            ls.append(node.val)

        self.travel(node.left, ls)
        self.travel(node.right, ls)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # if not root1 and root2:
        #     return False
        # if not root2 and root1:
        #     return False
        # if not root1 and root2:
        #     return True

        ls1 = []
        ls2 = []

        self.travel(root1, ls1)
        self.travel(root2, ls2)

        return ls1 == ls2
