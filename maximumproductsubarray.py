class Solution:

     def aVeryBigSum(self,ar):
        length = len(ar)
        strnum = ''
        for i in ar:
            num = str(i)[::-1]
            # print(i)
            lenstr = len(str)
            k = lenstr-1
            carry = 0
            for j in num:
                sum = int(strnum[k])+int(j)
                if(sum>9):
                    carry = int(sum/10)
                    sum = sum%10
                else:
                    carry = 0
                sum[k] = int(sum[k])+sum)
                sum[k-1]
                if(k ==0):
                    break;
                k = k-1

     def maxProduct(self, nums):
         length = len(nums)
         if(length==1):
             return nums[0]
         elif length == 0:
             return 0
         rec = [0]*length

         rec[0] = nums[0]
         prevmax = 1

         for i in range(1,length) :
             prod = rec[i-1]*nums[i]
             if(prod<0):

                 if(prevmax*nums[i]>0 and prevmax*nums[i]>prod):
                     rec[i] = max(prevmax*nums[i],nums[i])
                     prevmax = prod

                 else:
                     print('here2===',rec[i-1],nums[i],prevmax,(prevmax*nums[i]))

                     rec[i] = max(prod,(prevmax*nums[i]))
                     prevmax = nums[i]
                     print(i,'=====prevmax==========',prevmax)
                 print(i,'========',prevmax)
             else:
                 rec[i] = max(nums[i],rec[i-1]*nums[i])
             # print(i,':',rec[i],'prevmax',prevmax)

         print(rec)
         return max(rec)




obj = Solution()
obj.aVeryBigSum([10000005])
# nums = [2,3,-2,4]
# # nums = [-2,0,-1]
# # nums = [-2]
# # nums = [-4,-3]
# # nums = [2,3,-2,5,-1,2,3,-1,8]
#         # 2,6,-2,5,-1,
# nums = [-2,3,-4] #-6
#          # -2,3
# # nums = [7,-2,-4]
#         # 2,-3,2
# nums = [2,-5,-2,-4,3]
#         # 2,-5,20,
#         # 2,-5,
#         # 2,-5 ,10,
# obj.maxProduct(nums)
