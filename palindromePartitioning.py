class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        res = []
        
        def isPalindrome(word):
            for i in range(len(word)//2):
                if word[i] != word[-i - 1]:
                    return False
            return True
        
        def bt(P, idx = n - 1, valid = True):
            if idx == -1 and valid:
                res.append(P)
                return
            elif idx == -1:
                return
            cur = P[0]

            if isPalindrome(s[idx] + cur):
                tmp = ['']* len(P)
                for i in range(len(P)):
                    if i == 0:
                        tmp[0] = s[idx] + cur
                    else:
                        tmp[i] = P[i]
                bt(tmp, idx - 1, True)
            else:
                tmp = ['']* len(P)
                for i in range(len(P)):
                    if i == 0:
                        tmp[0] = s[idx] + cur
                    else:
                        tmp[i] = P[i]
                bt(tmp, idx - 1, False)
            if valid:
                P = [s[idx]] + P
                bt(P, idx - 1, True)
            
        bt([s[-1]], n-2)
        # github test
        return res
                