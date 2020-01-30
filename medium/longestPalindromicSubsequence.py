class Solution:
    def longestPalindromeSubseq(self, s):
        dp = []
        A = s
        B = s
        length = len(s)
        print(A)
        print(B)
        print(length)
        for i in range(0,len(s)):
            dp.append([0]*len(s))


        for i in range(0,length):
            dp[i][i] = 1
        # l=1
        # print(dp)
        for i in range(0,length):
            for j in range(i,-1,-1):
                if(A[i]!=B[j]):
                    if(j-1>=0 and i+1<length):
                        dp[i][j] = max(dp[i][j-1],dp[i+1][j])
                    elif(j-1<0):
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 2 + max(dp[i])
        # print(dp)
        for i in range(0,length):
            print(dp[i])




obj = Solution()
s = 'bbbab'
obj.longestPalindromeSubseq(s)
