class Solution:
    def sumRec(self,sum,n,i,count):
        # print('test')
        print(sum)
        if(sum==n):
            return sum
        sum += self.sumRec(sum,n,i+1,count)
        return i*i

    def numSquares(self, n):
        dp = []
        if(n==0 or n==1 or n==2 or n==3 ):
            return n
        for i in range(n+1):
            dp.append(0)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        dp[3]=3
        for i in range(4,n+1):
            dp[i]=i
            for x in range(1,(i*i)+1):
                tmp = x*x
                if(tmp>i):
                    break
                dp[i]=min(dp[i],1+dp[i-tmp])

        return dp.pop()



obj = Solution()
n = 2
obj.numSquares(n)
