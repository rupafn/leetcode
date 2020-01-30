class Solution:
    def uniquePaths(self, m, n):
        grid = []
        if(m==1):
            return 1
        for i in range(m):
            g = []
            for j in range(n):
                g.append(0)
            grid.append(g)
        grid[0][1] = 1
        grid[1][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                if(i>0 and j>0):
                    grid[i][j] += grid[i-1][j]+grid[i][j-1]
                elif(i==0 and j>0):
                    grid[i][j] += grid[i][j-1]
                elif(i>0 and j==0):
                    grid[i][j]+= grid[i-1][j]
        # print(grid)
        # print(grid[m-1][n-1])
        return grid[m-1][n-1]

obj = Solution()
m = 3
n=2
m = 7
n = 3
obj.uniquePaths(m,n)
