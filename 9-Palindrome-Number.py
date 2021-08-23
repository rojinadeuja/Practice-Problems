'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = 2**31 - 1
        reverse = 0
        while x != 0:
            digit = x % 10
            if reverse > (limit - digit) // 10:
                return 0
            reverse = reverse  * 10 + digit
            x = x // 10
        return reverse

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or self.reverse(x) != x:
            return False
        return True

# RC: O(n); SC:O(n)

# Solution by converting to String
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         x = str(x)
#         start = 0
#         end = len(x) - 1
#         while start < end:
#             if x[start] != x[end]:
#                 return False
#             else:
#                 start += 1
#                 end -= 1
#         return True
# # RC: O(n), SC: O(n)