class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for word in strs:
            new_prefix = ""
            if len(word) < len(prefix):
                letters = len(word)
            else:
                letters = len(prefix)
            for i in range(letters):
                if word[i] == prefix[i]:
                    new_prefix += word[i]
                else:
                    break
            prefix = new_prefix
            if prefix == "":
                break
        return prefix