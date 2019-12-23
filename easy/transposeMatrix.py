class Solution:
    def transpose(self, A):
        rowL = len(A)
        colL = len(A[0])
        newA = []
        for i in range(0,colL):
            listt = []
            for j in range(0,rowL):
                listt.append(A[j][i])
            newA.append(listt)
        return newA

obj = Solution()
A = [[1,2,3],[4,5,6],[7,8,9]]
A = [[1,2,3],[4,5,6]]
obj.transpose(A)
