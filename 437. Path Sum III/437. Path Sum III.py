from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The method so slowly and complexi0ty
class Solution1:
    def travel(self, node, targetSum):
        if not node:
            return 0

        # Check if the current node's value is equal to the remaining target sum
        count = 1 if node.val == targetSum else 0

        # Recursively explore left and right subtrees
        count += self.travel(node.left, targetSum - node.val)
        count += self.travel(node.right, targetSum - node.val)

        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # Start traversal from the root
        count = self.travel(root, targetSum)

        # Recursively explore left and right subtrees
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)

        return count


# Time: 43 ms (90.92%), Space: 16.98 MB (91.67%)
class Solution2:
    def travel(self, node, targetSum):
        if not node:
            return 0

        # Check if the current node's value is equal to the remaining target sum
        count = 1 if node.val == targetSum else 0

        # Recursively explore left and right subtrees
        count += self.travel(node.left, targetSum - node.val)
        count += self.travel(node.right, targetSum - node.val)

        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # Start traversal from the root
        count = self.travel(root, targetSum)

        # Recursively explore left and right subtrees
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)

        return count
