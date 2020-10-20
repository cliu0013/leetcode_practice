class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        n = len(height)
        i = 0
        j = n - 1
        while i != j:
            vol = (j - i) * min(height[i], height[j])
            res = max(res, vol)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return res
            
        