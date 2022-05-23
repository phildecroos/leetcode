class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack += char
            elif char == ")" or char == "]" or char == "}":
                if stack == []:
                    return False
                if (stack[-1] + char == "()") or (stack[-1] + char  == "[]") or (stack[-1] + char  == "{}"):
                    stack.pop()
                else:
                    return False
        if stack != []:
            return False
        return True