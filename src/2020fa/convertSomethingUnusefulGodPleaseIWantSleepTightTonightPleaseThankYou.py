class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        dic = {'1': 1,
               '2': 2,
               '3': 3,
               '4': 4,
               '5': 5,
               '6': 6,
               '7': 7,
               '8': 8,
               '9': 9,
               '0': 0
               }
        
        def convert(s1, s2):
            cur = 0
            while s != "":
                cur *= 10
                incre = dic[s[0]]
                cur += incre
                s = s[1:]
            return cur
        
        num1 = convert(num1)
        num2 = convert(num2)
        
        return str(num1 + num2)