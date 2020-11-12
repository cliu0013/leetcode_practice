class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        k = n - 1
        x_range = int(k/2.0 + 1)
        if n % 2 == 1:
            y_range = x_range - 1
        else:
            y_range = x_range
        
        for x in range(0, x_range):
            for y in range(0, y_range):
                matrix[x][y], matrix[y][k - x], matrix[k - x][k - y], matrix[k - y][x] = matrix[k - y][x], matrix[x][y], matrix[y][k - x], matrix[k - x][k - y]
                
        
