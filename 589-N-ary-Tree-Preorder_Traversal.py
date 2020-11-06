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
        
        if not root:
            return result
        
        def dfs(root):
            result.append(root.val)
            
            if not root.children:
                return
            
            if root.children:
                for child in root.children:
                    dfs(child)
        dfs(root)
        return result