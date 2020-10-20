class Solution(object):
     def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]
        
        def divided(n, count):
            if count == 1:
                return n in square_nums
            for num in square_nums:
                if divided(n - num, count - 1):
                    return True
            return False
        
        for i in range(1, n + 1):
            if divided(n, i):
                return i