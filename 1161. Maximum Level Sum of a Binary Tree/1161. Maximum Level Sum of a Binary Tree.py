# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: 170 ms (32.86%), Space: 19.84 MB (92.89%)
class Solution1:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def helper(node, level):
            if node:
                self.level[level] += node.val
                helper(node.left, level + 1)
                helper(node.right, level + 1)

        self.level = defaultdict(int)
        helper(root, 1)
        return sorted(self.level.items(), key=lambda x: x[1], reverse=True)[0][0]


# Time: 127 ms (99.94%), Space: 20.09 MB (54.40%)
class Solution2:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []
        q = [root]
        while q:
            sm = 0
            children = []
            for x in q:
                if x.left:
                    children.append(x.left)
                if x.right:
                    children.append(x.right)
                sm += x.val
            q = children
            levels.append(sm)
        return levels.index(max(levels)) + 1
