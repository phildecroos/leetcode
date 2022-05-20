class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digvals = []
        output = 0
        for i in range(len(s)):
            dig = s[i]
            if (dig == "M"):
                digvals.append(1000)
            elif (dig == "D"):
                digvals.append(500)
            elif (dig == "C"):
                digvals.append(100)
            elif (dig == "L"):
                digvals.append(50)
            elif (dig == "X"):
                digvals.append(10)
            elif (dig == "V"):
                digvals.append(5)
            elif (dig == "I"):
                digvals.append(1)
        for i in range(len(digvals)):
            if i < (len(digvals) - 1) and digvals[i+1] <= digvals[i]:
                output += digvals[i]
            elif i < (len(digvals) - 1):
                # do the subtraction thing
                output -= digvals[i]
            else:
                output += digvals[i]
        return output