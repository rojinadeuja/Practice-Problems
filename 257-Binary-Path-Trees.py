'''
Leetcode Q257 - https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        
        def dfs(root, path):
            if not root.left and not root.right:
                result.append(path)
                return
            if root.left:
                dfs(root.left, path + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, path + '->' + str(root.right.val))
                
        # Check if tree is empty
        if not root:
            return result
        
        # Run DFS on tree
        dfs(root, str(root.val))
        
        return result
            