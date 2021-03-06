class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m, n = len(board), len(board[0])
        seen = [[False]*(n) for _ in range(m)]
        
        def dfs(x, y, idx):
            if board[x][y] != word[idx] or seen[x][y] == True:
                return False
            if idx == len(word) - 1:
                return True
              
            seen[x][y] = True
            hor, ver = range(max(0, x - 1), min(x + 2, m)), range(max(0, y - 1), min(y + 2, n))
            if any(dfs(i , y , idx + 1) for i in hor) or any(dfs(x , j , idx + 1) for j in ver):
                return True
                
            seen[x][y] = False
            return False
                
        return any(dfs(i , j , 0) for i in range(m) for j in range(n))
            
        
        
        