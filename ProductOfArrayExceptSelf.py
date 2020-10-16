class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Left right product, O(n) runtime, O(1) extra time other than the result
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            # initializa the L in the result, no extra space
            res[i] = nums[i - 1]* res[i-1]
        R = 1
        for i in range(1, n+1):
            res[-i] *= R
            R *= nums[-i]
        return res
        