class Solution:
    def findFirstNegIndex(self, arr):
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
        negativeNumbers = 0
        for row in grid:
            firstNegIndex = self.findFirstNegIndex(row)
            negativeNumbers += (len(row)-firstNegIndex) if firstNegIndex != None else 0
        return negativeNumbers