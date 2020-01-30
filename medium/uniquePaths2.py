class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if(obstacleGrid[0][0]==1):
            return 0
        m = len(obstacleGrid)

        n = len(obstacleGrid[0])
        flag = False
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if(obstacleGrid[i][j]==1):
                    flag = True
                    obstacleGrid[i][j] = 'X'
        if(len(obstacleGrid)==1):
            if('X' in obstacleGrid[0]):
                return 0
            else:
                return 1
        if(n==1 and flag):
            return 0
        elif(n==1 and not flag):
            return 1
        if(obstacleGrid[0][1]!='X'):
            obstacleGrid[0][1] = 1
        if(obstacleGrid[1][0]!='X'):
            obstacleGrid[1][0]=1
        for i in range(0,len(obstacleGrid)):
            for j in range(0,len(obstacleGrid[i])):
                if(obstacleGrid[i][j]!='X'):

                    if(i>0 and j>0 and (obstacleGrid[i][j-1]!='X' and obstacleGrid[i-1][j]!='X')):

                        obstacleGrid[i][j] += obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                    elif(j>0 and obstacleGrid[i][j-1]!='X'):

                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
                    elif(i>0  and obstacleGrid[i-1][j]!='X'):

                        obstacleGrid[i][j]+= obstacleGrid[i-1][j]
        # print(obstacleGrid)
        if(obstacleGrid[m-1][n-1]=='X'):
            return 0
        return obstacleGrid[m-1][n-1]
input = [[0,0,0],[0,1,0],[0,0,0]]
input = [[1]]
input = [[0]]
input = [[0,0],[1,0]]
obj = Solution()
print(obj.uniquePathsWithObstacles(input))
