# Definition for a binary tree node
# class TreeNode (self, val=0, left=None, right=None):
#     self.val = val 
#     self.left = left
#     self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        if not root:
            return None
        
        # print("Root is",root.val)
          
        if root.val < low:
            # Process only its right
            return self.trimBST(root.right, low, high)
            
        elif root.val > high:
            # Process only its left
            return self.trimBST(root.left, low, high)
            
        else:
            # Root is okay in it's place
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root