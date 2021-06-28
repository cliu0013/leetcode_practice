class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         pre = [ 1 for i in range(n)]
#         cur = [ 1 for j in range(n)]
        
#         iter = 0
#         while iter < m - 1:
#             temp = cur
#             for i in range(1, n):
#                 cur[i] = cur[i - 1] + pre[i] 
#             pre = temp
#             iter += 1
        
#         return cur[n - 1]
        x = m + n - 2
        y = m - 1
        
        temp = 1
        for i in range(1, m):
            temp *= i
        de = temp
        
        temp = 1
        for i in range(m - 1):
            temp *= x - i
        nu = temp
        return nu//de
