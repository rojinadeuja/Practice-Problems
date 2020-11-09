'''
Leetcode Q344- https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s)-1
        # Swap elements alongside two ends of array
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1