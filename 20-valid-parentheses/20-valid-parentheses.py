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
            
        
        # for i in range(len(s)):
        #     char = s[i]
        #     if char == "(" or char == "[" or char == "{":
        #         for j in range(i, len(s)):
        #             if ((j - i) % 2 != 0) and ((char + s[j] == "()") or (char + s[j] == "[]") or (char + s[j] == "{}")):
        #                 if j - i == 1:
        #                     break
        #                 news = s[(i+1):(j-1)]
        #                 if not self.isValid(news):
        #                     return False
        #             elif j == len(s) - 1:
        #                 return False
        # return True
    
    
        '''
        pairs = []
        for i in s:
            pairs.append(False)
        for i in range(len(s)):
            print(pairs)
            if pairs[i] == False:
                char = s[i]
                if char == "(" or char == "[" or char == "{":
                    for j in range(i, len(s)):
                        if ((j - i) % 2 != 0) and ((char + s[j] == "()") or (char + s[j] == "[]") or (char + s[j] == "{}")):
                            for k in range(i, j + 1):
                                if pairs[k] == True:
                                    return False
                            pairs[j] = True
                            pairs[i] = True
                            break
                        elif j == len(s) - 1:
                            return False
                elif char == ")" or char == "]" or char == "}":
                    return False
        return True
        '''