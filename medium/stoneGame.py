class Solution:

    def stoneGame(self, piles):
        dp = []
        l = len(piles)
        for i in range(0,l):
            listt = []
            for j in range(0,l):
                obj = {
                "p1":0,
                "p2":0
                }
                if(i==j):
                    obj = {
                    "p1":piles[i],
                    "p2":0
                    }
                listt.append(obj)
            dp.append(listt)

        c = 1
        j = 0
        while(c<l):
            for i in range(j,l-c):
                p = piles[i:i+c+1]
                ll = len(p)
                if(p[0]>=p[-1]):
                    dp[i][i+c]['p1'] = p[0]+dp[i+1][i+c]['p2']
                    if(len(p)>2):
                        dp[i][i+c]['p2'] = p[-1]+dp[i][i+c-1]['p1']
                    else:
                        dp[i][i+c]['p2'] = p[-1]
                else:
                    # print(i,i+c,":",p[-1],dp[i][i+c-1]['p2'],p[-1]+dp[i][i+c-1]['p2'])
                    print(i,i+c,":",p[0],dp[i+1][i+c]['p1'])
                    dp[i][i+c]['p1'] = p[-1]+dp[i][i+c-1]['p2']
                    if(len(p)>2):
                        dp[i][i+c]['p2'] = p[0]+dp[i+1][i+c]['p1']
                    else:
                        dp[i][i+c]['p2'] = p[0]


            j=0
            c+=1
        for i in range(0,l):
            print(dp[i])
        if(dp[0][l-1]['p1']>=dp[0][l-1]['p2']):
            return True
        return False





obj = Solution()
piles = [5,3,4,5]
# piles = [4,2,10,9]
obj.stoneGame(piles)
