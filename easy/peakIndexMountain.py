class Solution:
    def peakIndexInMountainArray(self, A):
        for i in range(1,len(A)):
            if(A[i]<A[i-1]):
                return i-1

obj = Solution()
A = [0,1,0]
A = [0,2,1,0]
print(obj.peakIndexInMountainArray(A))
