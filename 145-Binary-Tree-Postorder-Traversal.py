'''
Leetcode Q145 - https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Check if no nodes to be processed
        if not root:
            return []
        # Traverse in Postorder (Left, Right, Root)
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]