class Solution:
    def find(self,s,dp,i):
        if(i == len(s)):
            return dp

        if(s[i]==')' and s[i-1]=="("):
            # print('cond1',i,s[i])
            if(i>=2):
                dp[i] = dp[i-2]+2
            else:
                dp[i] = 2

        elif(s[i]==')'  and s[i-1]==')' ):
            if(i%2==0):
                dp[i] = dp[i-dp[i]]+2
            # print(i)
            # # if(s[i-dp[i-1]]=='('):
            # print('dp[i-1]:',dp[i-dp[i-1]-2])
            # # dp[i] = dp[i-dp[i-1]-2]+2
            #
            # dp[i] = dp[i-dp[i]]+2

        return self.find(s,dp,i+1)


    def longestValidParentheses(self, s: str) -> int:
        if(len(s)==0):
            return 0
        dp = [0]*len(s)

        ans = self.find(s,dp,0)
        print(s)
        print(ans)
        # ans = list(filter(lambda a: a != 0, ans))
        return max(ans)

A = ')()())'
# A = "(()"
# A = "()(())("
# A= "(()"
# A = ")()())"
# A = "())"
# A = "()(())"
# A= "(()())"
# # A = "(()))())("
# A = ")()())"
A = "()(())"
# A = "()()"
# A = "())"
# A = "((()))())"
# A = ')( '
# A = ")(((((()())()()))()(()))("
print(len(A))
obj = Solution()
obj.longestValidParentheses(A)
