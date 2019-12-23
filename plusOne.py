class Solution:
    def plusOne(self, digits):
        strs = ''
        for i in digits:
            strs+= str(i)
        strs = str(int(strs)+1)
        return list(strs)



obj = Solution()

input = [1,2,3]
input = [4,3,2,1]
print(obj.plusOne(input))
