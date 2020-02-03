class Solution:
    def kWeakestRows(self, mat, k):
        sums = []
        for i in range(0,len(mat)):
            sums.append(sum(mat[i]))
        res = []
        while(k>0):
            ind = sums.index(min(sums))
            sums[ind] = 100000
            res.append(ind)
            k-=1
        return res


obj = Solution()
mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
obj.kWeakestRows(mat,k)
