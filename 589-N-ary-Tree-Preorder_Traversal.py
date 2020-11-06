'''
Leetcode Q589-https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Given an n-ary tree, return the preorder traversal of its nodes' values.
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:               
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        # If tree is empty return empty list
        if not root:
            return result
        # Define Depth First Search
        def dfs(root):
            result.append(root.val)
            
            if not root.children:
                return
            
            if root.children:
                for child in root.children:
                    dfs(child)
        # Carry out DFS
        dfs(root)
        return result

# Time complexity for DFS is O(V+E). Space complexity is constant, O(V).