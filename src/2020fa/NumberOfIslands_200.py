class Solution(object):
    def numIslands(self, grid):
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num += 1
                    self.dfs(i,j,grid)
        return num
    
    def dfs(self, i, j, grid):
        # Use recursice DFS
        # When does edge demonishes
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        else:
            # set visited and visit the children
            grid[i][j] = "0"
            self.dfs(i, j-1, grid)
            self.dfs(i, j+1, grid)
            self.dfs(i-1, j, grid)
            self.dfs(i+1, j, grid)

        