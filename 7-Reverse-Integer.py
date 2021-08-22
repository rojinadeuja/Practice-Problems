'''
Leetcode Q7 - https://leetcode.com/problems/reverse-integer/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
''' 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            x *= -1
            sign = -1
            
        limit = 2**31 - 1
        reverse = 0
        while x != 0:
            digit = x % 10
            if reverse > (limit - digit) // 10:
                return 0
            reverse = reverse  * 10 + digit
            x = x // 10
            
        return sign * reverse
# RC: O(n) where n is digits in x; SC: O(n)