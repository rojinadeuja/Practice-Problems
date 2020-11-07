# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Check if more nodesto be processed
        if not root:
            return []
        # Traverse in Preorder (Root, Left, Right)
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)