class Solution:
    def divisorGame(self, N):
        dp = [False]*N
        dp[0] = False
        dp[1] = False
        for i in range(1,N):
            for j in range(1,i):
                if(i%j==0):
                    if(dp[i-j]==False):
                        dp[i] = True
                        break
        print(dp)
        return dp[N-1]




obj = Solution()
N = 2
print(obj.divisorGame(N))
