# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        self.maxCount = 0
        self.dct = {}
        self.mode = []
        
        def findCount(root):
           
            if not root:
                return
            
            if root.val not in self.dct:
                self.dct[root.val] = 1
            else:
                self.dct[root.val] += 1
            
            if root.left:
                findCount(root.left)
                
            if root.right:
                findCount(root.right)
                
            if self.dct[root.val] >= self.maxCount:
                self.maxCount = self.dct[root.val]
                
            if not root.right and not root.left:
                self.count = 1
            
        
        findCount(root)
        
        for key, val in self.dct.items():
            if val == self.maxCount:
                self.mode.append(key)
                
        return self.mode