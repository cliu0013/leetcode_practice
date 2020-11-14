class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        n = len(nums)
        if n == 0: return 0
        
        dp = [0] * n
        def bt(idx):
            cur = nums[idx]
            res = 1
            for i in range(idx + 1, n):
                if cur < nums[i]:
                    res = max(res, 1 + dp[i])
            dp[idx] = res
            
        i = n - 1
        while i != -1:
            bt(i)
            i -= 1
        
        return max(dp)
                
            
        