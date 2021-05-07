class Solution:
    def findDuplicates(self, nums):
        dict = {}
        dups = []
        for i in nums:
            if(i not in dict):
                dict[i] = 1
            elif(dict[i]==1):
                dict[i]+=1
                dups.append(i)

        return dups


obj = Solution()
nums = [4,3,2,7,8,2,3,1]
obj.findDuplicates(nums)
