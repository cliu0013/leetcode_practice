class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # O(4^n), O(4^n)
        dic = {"2":"abc",
               "3":"def",
               "4":"ghi",
               "5":"jkl",
               "6":"mno",
               "7":"pqrs",
               "8":"tuv",
               "9":"wxyz"}
        
        n = len(digits)
        if n == 0:
            return []
        k = 1
        res = [""]
        for digit in digits:
            new_res = []
            for char in dic[digit]:
                for st in res:
                    new_res.append(st + char)
            res = new_res
        return res
            