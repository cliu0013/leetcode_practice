class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Space complexity is O(1) as there are only 26 lowercase english letters
        
        if len(s) != len(t):
            return False
        
        dic = collections.Counter(s)
        dic_2 = collections.Counter(t)
        for key in dic:
            if key not in dic_2:
                return False
            elif dic[key] != dic_2[key]:
                return False
        
        
        
        return True
        