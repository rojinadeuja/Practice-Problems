class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if haystack == '':
            return -1
        n = len(needle)
        for i in range(len(haystack)-(n-1)):
            if haystack[i:i+n] == needle:
                return i
        return -1
# Time complexity will be O(n). Space complexity will be O(1)  