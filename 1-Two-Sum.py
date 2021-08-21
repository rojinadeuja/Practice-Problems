'''
Leetcode Q1 -https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

# # Brute-Force
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         result = []
#         for i in range(0, len(nums)):
#             for j in range(1, len(nums)-1):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     result.append(i)
#                     result.append(j)
#         return result
#     # Run time complexity O(n*n), Space complexity O(1)
                
        
# Optimized
class Solution(object):
    def twoSum(self, nums, target):
        numsPrev = []
        # Create a array with number and index
        for i, num in enumerate(nums):
            numsPrev.append((num, i))
        numsPrev.sort()
        
        p1 = 0
        p2 = len(nums)-1
        
        while p1<p2:
            if numsPrev[p1][0] + numsPrev[p2][0] == target:
                return [numsPrev[p1][1], numsPrev[p2][1]]
            elif numsPrev[p1][0] + numsPrev[p2][0] > target:
                p2-=1
            else:
                p1+=1
        return []
# RC: O(n log n); SC: O(n)