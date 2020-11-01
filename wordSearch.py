class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if len(board) == 0:
            return False
        
        m = len(board)
        n = len(board[0])
        
        
        
        padded_board = [[""]*(n+2) for _ in range(m+2)]
        seen = [[False]*(n+2) for _ in range(m+2)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                padded_board[i][j] = board[i-1][j-1]
        print(padded_board)
        length = len(word)
        
        def check(pos, idx):
            x, y = pos[0], pos[1]
            if padded_board[x][y] != word[idx] or seen[x][y] == True:
                return False
            if padded_board[x][y] == word[idx] and idx == len(word) - 1:
                return True    
                
            seen[x][y] = True
            if padded_board[x][y] == word[idx]:
                for i in range(x - 1, x + 2):
                    if check([i, y], idx + 1):
                        return True
                for j in range(y - 1, y + 2):
                    if check([x, j], idx + 1):
                        return True
                
            seen[x][y] = False
            return False
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if check([i, j], 0):
                    return True
                
        return False
            
        
        
        