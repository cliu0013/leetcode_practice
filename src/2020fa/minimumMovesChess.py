class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # (1) one direction BFS with pruning
        # time complexity O(|x|*|y|)
    
        x, y = abs(x), abs(y)
        
        self.visited = {(0, 0): 0}
        self.stack = [(0, 0)]        
        d = 0
        
        def helper(pos, d):
            
            x_cur, y_cur = pos[0], pos[1]
            res = [(x_cur - 2, y_cur - 1),(x_cur - 1, y_cur - 2),(x_cur + 2, y_cur - 1),(x_cur + 1, y_cur - 2),(x_cur - 2, y_cur + 1),(x_cur - 1, y_cur + 2),(x_cur + 2, y_cur + 1),(x_cur + 1, y_cur + 2)]
            for ele in res:
                if ele not in self.visited and -1 <= ele[0] <= x+2 and -1 <= ele[1] <= y+2:
                    self.visited[ele] = d + 1
                    self.stack.append(ele)
            
        
        while self.stack:
            cur = self.stack.pop(0)
            if cur[0] == x and cur[1] == y:
                return self.visited[cur]
            else:
                helper(cur, self.visited[cur])
        
        # (2) DP+ memoization
        # @lru_cache(None) 
        # def dp(x,y):
        #     if x + y == 0: return 0
        #     elif x + y == 2: return 2
        #     return min(dp(abs(x-1),abs(y-2)), dp(abs(x-2),abs(y-1))) + 1
        # return dp(abs(x),abs(y))
        
        # (3) math
        # x, y = abs(x), abs(y)
        # if (x < y): x, y = y, x
        # if (x == 1 and y == 0): return 3        
        # if (x == 2 and y == 2): return 4        
        # delta = x - y
        # if (y > delta): return delta - 2 * int((delta - y) // 3);
        # else: return delta - 2 * int((delta - y) // 4);
        
        
    
       
            
        