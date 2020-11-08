'''
Leetcode Q669- https://leetcode.com/problems/trim-a-binary-search-tree/

Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
trim the tree so that all its elements lies in [low, high]. 
Trimming the tree should not change the relative structure of the elements that will remain in the tree 
(i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
'''

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