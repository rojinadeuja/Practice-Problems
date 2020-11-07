# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Check if tree is empty
        if not root:
            return root
        
        def traverseNodes(root: TreeNode):
            # Check if no more nodes to traverse
            if not root:
                return []
            # Traverse nodes In-order
            return traverseNodes(root.left) + [root.val] + traverseNodes(root.right)
            