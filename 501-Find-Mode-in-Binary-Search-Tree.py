'''
Leetcode Q501- https://leetcode.com/problems/find-mode-in-binary-search-tree/

Given a binary search tree (BST) with duplicates, 
find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
'''
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
            # If root is None return
            if not root:
                return
            
            # If value not in dict, put into dict. Else, increase count
            if root.val not in self.dct:
                self.dct[root.val] = 1
            else:
                self.dct[root.val] += 1
            
            # If left exists, go left
            if root.left:
                findCount(root.left)
            
            # If right exists, go right
            if root.right:
                findCount(root.right)

            # Find max count  
            if self.dct[root.val] >= self.maxCount:
                self.maxCount = self.dct[root.val]

        # Run findCount() function
        findCount(root)
        
        # Get all nodes with max fount from dictionary
        for key, val in self.dct.items():
            if val == self.maxCount:
                self.mode.append(key)
                
        return self.mode