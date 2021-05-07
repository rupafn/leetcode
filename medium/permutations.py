class Solution:
    def perm2(self, s,mem,str,l):
        print(str)
        if(len(str)==l):
            mem.append(str)
        length = len(s)
        for i in range(0,length):
            # if(s[i] not in str):
            choice =str+[s[i]]
            options = s[0:i]+s[i+1:length]
            self.perm2(options,mem,choice,l)
        return mem

    def permute(self, nums):

        listt = []
        length = len(nums)
        # if(len(nums)==1):
        #     return [nums]
        for i in range(0,len(nums)):
            listt+=self.perm2(nums,[],[nums[i]],length)
        return listt


input = [1,2,3,4,5]
# input = [0]
# input = [1,2]

obj = Solution()
print(obj.permute(input))
