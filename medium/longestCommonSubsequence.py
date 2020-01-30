class Solution:
    def longestCommonSubsequence(self, text1, text2):
        A = text1
        B = text2
        dp = []
        for j in range(len(A)):
            dp.append([0]*len(B))

        for i in range(0,len(A)):
            for j in range(0,len(B)):
                if(A[i] == B[j]):
                    if(i-1>=0 and j-1>=0):
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = 1
                else:
                    if(j-1>=0 and i-1>=0):
                        dp[i][j] = max(dp[i][j-1],dp[i-1][j])
                    elif(j-1<0 and i-1<0):
                        dp[i][j] = 0
                    elif(j-1<0 and i-1>=0):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]
        return dp[len(A)-1][len(B)-1]






obj = Solution()
text1 = "abcde"
text2 = "ace"
text1 = "abc"
text2 = "abc"
# text1 = "abc"
# text2 = "def"
text1 = "hofubmnylkra"
text2 = "pqhgxgdofcvmr"
obj.longestCommonSubsequence(text1,text2)
