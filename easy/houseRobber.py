class Solution:
    def rob(self, nums):

        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for j in range(2,len(nums)):
            dp[j] = max(nums[j]+dp[j-2],dp[j-1])

        return max(dp)

# nums = [1,2,3,1]
nums = [2,7,9,3,1]
# nums = []
# nums = [2,1,1,2]
obj = Solution()
print(obj.rob(nums))
