class Solution:
    def checkDuplicates(self, result, triplets):
        triplets.sort()
        newarr = []
        for r in result:
            r.sort()
            newarr.append(r)
        if(triplets in newarr):
            return True

        return False

    def threeSum(self, nums) :
        nums.sort()
        res = []
        for i in range(0,len(nums)):
            start = i+1
            end = len(nums)-1
            if(i>0 and nums[i]==nums[i-1]):
                continue
            while(start<end):
                if( end<len(nums)-1 and nums[end] == nums[end+1]):
                    end-=1
                    continue
                if(nums[i] + nums[start] + nums[end] == 0):
                    res.append([nums[i],nums[start],nums[end]])
                    start +=1
                    end -=1
                elif(nums[i] + nums[start] + nums[end] < 0):
                    start+=1
                else:
                    end-=1
        return res


obj = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [1,-1,-1,0]
obj.threeSum(nums)
