# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        
        # Computer median
        med = len(nums)//2
        
        # Add median of nums as root node
        root = TreeNode(nums[med])
        # Recursively add medians along subarrays to left and right
        root.left = self.sortedArrayToBST(nums[:med])
        root.right = self.sortedArrayToBST(nums[med+1:])
        
        return root