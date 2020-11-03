class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
        for k in range(1, int(upper_limit)):
            N -= k
            if N % k == 0:
                count += 1
        return count
        