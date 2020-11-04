class Solution:
    def isValid(self, s: str) -> bool:
        dct = {'(':')', '{':'}', '[':']'}
        stack = []
        if len(s)==1:
            return False
        for bracket in s:
            if bracket in dct:
                stack.append(bracket)
            else:
                if(stack and dct[stack[-1]] == bracket):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
                    