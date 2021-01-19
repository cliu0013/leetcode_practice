class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def checkRow(row):
            dic = {}
            for i in range(9):
                tar = board[row][i]
                if tar in dic:
                    return False
                if tar != ".":
                    dic[tar] = True
            return True
            
        def checkCol(col):
            dic = {}
            for i in range(9):
                tar = board[i][col]
                if tar in dic:
                    return False
                if tar != ".": 
                    dic[tar] = True
            return True
            
        def checkBlock(row, col):
            dic = {}
            i, j = 3 * row, 3 * col
            for k in range(3):
                for t in range(3):  
                    tar = board[i + k][j + t]
                    if tar in dic:
                        return False
                    if tar != ".": 
                        dic[tar] = True
            return True
        
        for i in range(9):
            if not checkRow(i) or not checkCol(i):
                return False
            
        for i in range(3):
            for j in range(3):
                if not checkBlock(i, j):
                    return False
                
        return True
            