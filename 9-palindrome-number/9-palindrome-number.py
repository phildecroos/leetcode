class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = ""
        if x < 0:
            return False
        for i in range(len(str(x))):
            reverse += str(x)[len(str(x)) - i - 1]
        if reverse == str(x):
            return True
        return False
        