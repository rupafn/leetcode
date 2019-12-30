class Solution:

    def recur(row,col,grid,sum):
        if(col==0 and row>0):
            sum+=grid[row-1][col]
            row = row-1
        elif(row==0 and col>0):
            sum+=grid[row][col-1]
            col = col-1
        else:
            if(grid[row-1][col]<grid[row][col-1]):
                sum+=grid[row-1][col]
                row = row-1
            else:
                sum+=grid[row][col-1]
                col = col-1


    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])

        if(row == 0 and col ==0):
            return grid[row][col]
        for i in range(row):
            for j in range(col):
                if i ==0 and j ==0:
                    continue
                grid[i][j] = grid[i][j]+min(grid[i-1][j] if i>0 else float('inf'), grid[i][j-1] if(j>0) else float('inf'))
        for i in range(row):
            print(grid[i])
        return grid[row-1][col-1]
        # print(sum)

obj = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid=[[0,1,1],[1,1,1]]
# grid = [[0]]
# grid=[[1,1],[1,1],[1,1]]
# grid = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]
obj.minPathSum(grid)
