# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        resultList = []
        innerList = []
        if not root:
            return resultList
        
        count = 1
        switch = False
        que = Queue()
        que.put(root)
        
        while not que.empty():
            root = que.get()
            count -= 1
           
            if root.left:
                que.put(root.left)
            if root.right:
                que.put(root.right)
           
            innerList.append(root.val)
            
            if count == 0:
                if switch:
                    innerList.reverse()
                resultList.append(innerList)
                innerList = []
                count = que.qsize()
                switch = not switch
        return resultList