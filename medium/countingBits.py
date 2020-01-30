class Solution:
    def countBits(self, num):
        p = 2
        dp = [0]*(num+1)
        s = 2
        i = 1

        while(i<=num):
            dp[i] = 1+dp[i-(p>>1)]
            i+=1
            if(i==p and i<=num):

                dp[i]=1
                i+=1
                p = 1<<s
                s+=1

        return dp



obj = Solution()
obj.countBits(127)
