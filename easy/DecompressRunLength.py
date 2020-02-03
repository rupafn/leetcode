class Solution:
    def decompressRLElist(self, nums):
        listt = []
        i = 0
        while(i<len(nums)):
            a = nums[i]
            b = nums[i+1]
            listt = listt + [b]*a
            i+=2
        return listt


obj = Solution()
nums = [1,2,3,4]
obj.decompressRLElist(nums)
