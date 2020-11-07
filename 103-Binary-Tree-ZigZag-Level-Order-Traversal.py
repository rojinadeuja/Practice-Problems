'''
Leetcode Q103 - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        innerList = []
        resultList = []

        # If tree is empty return empty list
        if not root:
            return []
        
        # Count number of nodes in each level, initialize 1 for root
        count = 1
        switch = False

        # Intialize queue
        que = Queue()
        # Put root into queue
        que.put(root)
        
        while not que.empty():
            # Pop a node and decrement count
            root = que.get()
            count -= 1
            # Add its children to queue
            if root.left:
                que.put(root.left)
            if root.right:
                que.put(root.right)
            # Add node to innerList
            innerList.append(root.val)

            # If no more nodes in level, add level to resultList
            if count == 0:
                # If switch, reverse the innerList
                if switch:
                    innerList.reverse()
                resultList.append(innerList)
                innerList = []
                count = que.qsize()
                # Toggle switch after each level
                switch = not switch

        return resultList

