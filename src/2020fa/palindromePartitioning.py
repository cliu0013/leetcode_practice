class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        res = []
        seen = set()
        
        def isPalindrome(word):
            if word == word[::-1]: return True
            return False
        
        def bt(P, idx = n - 1, valid = True):
            if idx == -1:
                if valid: res.append(P)
                return
         
            key = s[idx] + P[0]
            if key in seen or isPalindrome(key):
                seen.add(key)
                bt([key] + P[1:], idx - 1, True)
            else:
                bt([key] + P[1:], idx - 1, False)
            if valid:
                bt([s[idx]] + P, idx - 1, True)
            
        bt([s[-1]], n-2)
        return res
                