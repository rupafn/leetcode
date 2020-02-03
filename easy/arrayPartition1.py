class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        store = []
        while(len(nums)!=0):
            store.append((nums.pop(),nums.pop()))
        sum = 0
        print(store)
        for pair in store:
            sum += min(pair)
        return sum

obj = Solution()
nums = [1,4,3,2]
nums = [1,1,1,1]
print(obj.arrayPairSum(nums))
