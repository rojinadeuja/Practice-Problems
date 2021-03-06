'''
Leetcode Q704- https://leetcode.com/problems/binary-search/

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Use Binary Search on array
        start = 0
        end = len(nums)-1
        while start<=end:
            median = (start + end ) // 2
            # If found, return index
            if target == nums[median]:
                return median
            elif target > nums[median]:
                start = median + 1
            else:
                end = median - 1
        # If not found, return -1
        return -1

# Time Complexity using Binary Search is O(log n). Space complexity is constant O(1).