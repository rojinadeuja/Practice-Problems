class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            median = (start + end ) // 2
            if target == nums[median]:
                return median
            elif target > nums[median]:
                start = median + 1
            else:
                end = median - 1
        return -1