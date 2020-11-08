'''
Leetcode Q107 - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).
'''

# Definition for a binary tree node.
# class TreeNode(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

from queue import Queue
    
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        resultList = []
        innerList = []

        # If tree is empty return empty list
        if not root:
            return resultList

        count = 1
        que = Queue()
        que.put(root)
        
        while not que.empty():
            node = que.get()
            count -= 1
            
            if node.left:
                que.put(node.left)
            if node.right:
                que.put(node.right)
            
            innerList.append(node.val)
            
            # Check if level complete
            if count == 0:
                resultList.insert(0, innerList)
                innerList = []
                count = que.qsize()
        return resultList