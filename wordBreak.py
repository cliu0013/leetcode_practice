class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # # O(n^3) DP
        # dp = [True]*(len(s) + 1)
        # words = set(wordDict)
        # for i in range(1, len(s)+1):
        #     dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        # return dp[-1]
    
        # O(n^2) DFS
        memo = {}
        words = set(wordDict)
        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            for i in range(start+1, len(s)+1):
                if s[start:i] in words and dfs(i):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
    
        return dfs(0)
        