# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Check if more nodes to be processed
        if not root:
            return []
        # Traverse in Inorder (Left, Root, Right)
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)