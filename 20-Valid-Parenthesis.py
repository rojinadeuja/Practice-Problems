'''
Leetcode Q20 -https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        dct = {'(':')', '{':'}', '[':']'}
        stack = []
        if len(s)==1:
            return False
        for bracket in s:
            if bracket in dct:
                # If opening tag then push into stack
                stack.append(bracket)
            else:
                # If stack is not empty and last element is the closing tag for a bracket then pop out of stack
                if(stack and dct[stack[-1]] == bracket):
                    stack.pop()
                else:
                    return False
        # Return true only if stack is empty
        if not stack:
            return True
                    