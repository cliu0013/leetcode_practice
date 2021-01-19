class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        d = min(m, n)
        dp = [[] for _ in range(d)] 
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[0].append((i, j))
                    
               
        if len(dp[0]) == 0: return 0
        def step(size):
            for indice in dp[size - 2]:
                x, y = indice
                
                check_x, check_y = x + size - 1, y + size - 1
              
                if check_x < m and check_y < n:
                    
                    checkx = checky = True
                    for i in range(x, check_x + 1):
                        if matrix[i][check_y] != '1':
                            checkx = False
                            break
                    for j in range(y, check_y + 1):
                        if matrix[check_x][j] != '1':
                            checky = False
                            break

                    if checkx and checky:
                        dp[size - 1].append(indice)
        
        
        for i in range(2, d + 1):
            step(i)
            if len(dp[i - 1])== 0:
                return (i - 1)**2
            elif i == d:
                return d**2
        
        # print(dp)
        return 1
        
        
        
    
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if len(matrix) == 0:
#             return 0
    
#         n, m = len(matrix), len(matrix[0])
        
#         dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        
#         # smarter DP, see through how to utilize the most marginal output, dont do stupid dp
#         max_square = 0
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 if matrix[i-1][j-1] == "1":
#                     dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#                     max_square = max(max_square, dp[i][j])    
#         return max_square ** 2
