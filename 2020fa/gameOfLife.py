class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        if m == 0: return board
        n = len(board[0])
        if n == 0: return board
        
        def step(x, y):
            
            neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
            cur = board[x][y]
            lives = 0
            for neighbor in neighbors:
                dx, dy = neighbor[0], neighbor[1]
                new_x, new_y = x + dx, y + dy
                if new_x in range(m) and new_y in range(n):
                    state = board[new_x][new_y]
                    if state == 1 or state == 2:
                        lives += 1
            if cur == 1:
                if lives < 2 or lives > 3:
                    return 2
                else:
                    return 1
            if cur == 0:
                if lives == 3:
                    return 3
                else:
                    return 0
        
        for i in range(m):
            for j in range(n):
                board[i][j] = step(i, j)
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2 
        