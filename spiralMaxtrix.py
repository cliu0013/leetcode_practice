class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def oneShot(start, width, height, l = True):
            # print(start, width, height, l)
            if width == 0 or height == 0:
                return []
            col_left = start[1]
            col_right = start[1] + width -1 
            row_up = start[0]
            row_down = start[0] + height -1
            # print(col_left, col_right, row_up, row_down)
            res = []
            if l:
                res += matrix[row_up][col_left:col_right+1]
                for i in range(row_up + 1, row_down+1):
                    res += [matrix[i][col_right]]
                return res + oneShot([row_up + 1, col_left], width-1, height-1, False)
            else:
                res += matrix[row_down][col_left:col_right+1][::-1]
                count = row_down- 1
                while count >= row_up:
                    res += [matrix[count][col_left]]
                    count -= 1
                return res + oneShot([row_up, col_left+1], width-1, height-1, True)
        
        if len(matrix) == 0:
            return []
        return oneShot([0, 0], len(matrix[0]), len(matrix), l = True)