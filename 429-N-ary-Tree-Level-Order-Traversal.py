"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from queue import Queue

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        resultList = []
        innerList = []
        
        if not root:
            return resultList
        
        que = Queue()
        que.put(root)
        
        count = 1
        
        while not que.empty():
            node = que.get()
            count -= 1
            
            if node.children:
                children = node.children
                for child in children:
                    que.put(child)
                
            innerList.append(node.val)
            
            if count == 0:
                resultList.append(innerList)
                innerList = []
                count = que.qsize()
                
        return resultList