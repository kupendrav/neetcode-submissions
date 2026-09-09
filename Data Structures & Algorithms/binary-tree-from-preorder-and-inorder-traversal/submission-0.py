from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for quick lookup
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        # Iterator for preorder list
        preorder_iter = iter(preorder)
        
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements
            if left > right:
                return None
            
            # Next root from preorder
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Build left and right subtrees
            root.left = array_to_tree(left, inorder_index[root_val] - 1)
            root.right = array_to_tree(inorder_index[root_val] + 1, right)
            
            return root
        
        return array_to_tree(0, len(inorder) - 1)
