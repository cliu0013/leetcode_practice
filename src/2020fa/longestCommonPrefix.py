class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
    
        
        max_len = min([len(st) for st in strs])
        if not max_len: return ""
        
        count = 0
        while count < max_len:
            target = strs[0][count]
            for st in strs:
                if st[count] != target:
                    return st[:count]
            count += 1
        return strs[0][:count]
        