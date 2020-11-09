'''
Leetcode - https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''

# Approach 1
import re
class Solution:
    def isPalindrome(self, s:str) -> bool:
        if not str:
            return True
        s = re.sub(r'[\W_]+','',s).lower()
        start = 0
        end = len(s)-1
        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start +=1
                end -=1
        return True