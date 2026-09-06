# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            # Check if current node is good
            good = 1 if node.val >= max_val else 0
            # Update max value for children
            max_val = max(max_val, node.val)
            # Recurse left and right
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)
        
        return dfs(root, root.val)
