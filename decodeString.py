class Solution(object):
    dic = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #O(maxK n), O(n)
        if s == "":
            return s
        i = float("inf")
        j = float("inf")
        for pos, st in enumerate(s):
            if st == "[":
                i = pos
            elif st == "]":
                j = pos
                break
        if i == float("inf"):
            return s
        idx = i - 1
        while True:
            if idx - 1 < 0 or s[idx - 1] not in self.dic:
                break
            idx -= 1       
        s = s[0 : idx] + int(s[idx: i])*s[i + 1:j] + s[j + 1:]
        return self.decodeString(s)
        
            
        