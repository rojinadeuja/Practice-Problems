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
        
        # If tree is empty return empty list
        if not root:
            return resultList

        # Initialize queue
        que = Queue()
        que.put(root)
    
        count = 1
    
        while not que.empty():
            node = que.get()
            count -= 1
            # If node has children, put into queue
            if node.children:
                children = node.children
                for child in children:
                    que.put(child)
                
            innerList.append(node.val)

            # Check if level complete
            if count == 0:
                resultList.append(innerList)
                innerList = []
                count = que.qsize()
                
        return resultList