class Solution:
    def sortArrayByParity(self, A):

        odd = []
        even = []
        for i in A:
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)
        return even+odd


obj = Solution()
A = [3,1,2,4]
print(obj.sortArrayByParity(A))
