class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True]*(len(s) + 1)
        words = set(wordDict)
        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        return dp[-1]