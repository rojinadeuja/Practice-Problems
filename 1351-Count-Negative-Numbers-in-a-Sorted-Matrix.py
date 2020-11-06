'''
Leetcode Q1351- https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.
'''

class Solution:
    def findFirstNegIndex(self, arr):
        '''Function that returns the index of first negative number using Binary Search'''
        start = 0
        end = len(arr)-1

        while start<=end:
            median = (start+end)//2
            if arr[median]<0 and ((median>0 and arr[median-1]>=0) or median == 0):
                return median
            if arr[median] >= 0:
                start = median + 1   
            else:
                end = median - 1
      
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''Function to count negative numbers in array'''
        negativeNumbers = 0
        for row in grid:
            firstNegIndex = self.findFirstNegIndex(row)
            negativeNumbers += (len(row)-firstNegIndex) if firstNegIndex != None else 0
        return negativeNumbers