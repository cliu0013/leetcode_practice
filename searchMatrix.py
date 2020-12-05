class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # DFS
        
        # approach 4
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col <= n - 1:
            if matrix[row][col] < target:
                col += 1 
            elif matrix[row][col] > target:
                row -= 1
            else:
                print(matrix[row][col])
                return True
        
        return False
            
            