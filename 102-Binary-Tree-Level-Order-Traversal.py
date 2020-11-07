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
            root = que.get()
            count -=1
            if root.left:
                que.put(root.left)
            if root.right:
                que.put(root.right)
            innerList.append(root.val)
            if count == 0:
                resultList.append(innerList)
                innerList = []
                count = que.qsize()
        return resultList