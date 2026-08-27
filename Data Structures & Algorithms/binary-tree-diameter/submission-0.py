# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            # Recursively get left and right subtree heights
            left_height = height(node.left)
            right_height = height(node.right)

            # Update diameter: longest path through this node
            self.diameter = max(self.diameter, left_height + right_height)

            # Return height of this subtree
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter
