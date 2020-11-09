'''
Leetcode Q28 -https://leetcode.com/problems/implement-strstr/
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        n = len(needle)
        for i in range(len(haystack)-(n-1)):
            if haystack[i:i+n] == needle:
                return i
        return -1
# Time complexity will be O(n). Space complexity will be O(1)  