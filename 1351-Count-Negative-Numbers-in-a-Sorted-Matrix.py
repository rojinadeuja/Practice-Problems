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
            med = (start+end)//2
            if arr[med]<0 and ((med>0 and arr[med-1]>=0) or med == 0):
                return med
            if arr[med] >= 0:
                start = med + 1   
            else:
                end = med - 1
      
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''Function to count negative numbers in array'''
        negativeNumbers = 0
        for row in grid:
            firstNegIndex = self.findFirstNegIndex(row)
            negativeNumbers += (len(row)-firstNegIndex) if firstNegIndex != None else 0
        return negativeNumbers