# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        innerList = []
        resultList = []
        count = 1
        que = Queue()
        
        if not root:
            return []
        que.put(root)
        
        while not que.empty():
            e = que.get()
            count -=1
            if e.left:
                que.put(e.left)
            if e.right:
                que.put(e.right)
            innerList.append(e.val)
            if count == 0:
                resultList.append(innerList)
                innerList = []
                count = que.qsize()
        return resultList