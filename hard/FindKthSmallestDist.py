class Solution:
    def smallestDistancePair(self, nums, k):

        diff = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                diff.append(abs(nums[i]-nums[j]))
        # diff.sort()
        # print(diff)
        # return diff[k-1]


obj = Solution()

nums = [1,3,1]
k = 1
# nums = [1,6,1]
# k = 3
print(obj.smallestDistancePair(nums,k))
