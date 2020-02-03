class Solution:
    def oddCells(self, n, m, indices):
        matrix = []
        for i in range(n):
            matrix.append([0]*m)
        for i in indices:
            r = i[0]
            c = i[1]
            for j in range(0,len(matrix[r])):
                matrix[r][j]+=1
            for k in range(0,len(matrix)):
                matrix[k][c]+=1
        count = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(matrix[i][j]%2!=0):
                    count+=1
        return count


n = 2
m = 3
indices = [[0,1],[1,1]]

obj = Solution()
obj.oddCells(n,m,indices)
