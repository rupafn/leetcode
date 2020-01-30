class Solution:
    def minimumTotal(self, triangle):
        dp = [0]*len(triangle)
        dp[0] = triangle[0][0]
        minInd = 0
        for i in range(1,len(triangle)):

            minCost = 1000
            k = minInd
            for j in range(k,k+2):
                print(triangle[i][j],i,j)
                if(dp[i]+triangle[i][j]<minCost):
                    minCost =dp[i]+triangle[i][j]
                    minInd = j
            dp[i] = minCost
        print(dp)
        return sum(dp)



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1],[2,3],[1,-1,-3]]
obj = Solution()
obj.minimumTotal(triangle)
