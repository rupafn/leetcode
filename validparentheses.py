class Solution:

     def isValid(self,s):
         s = list(s)
         length = len(s)
         count = 0
         for i in range(0,length):
             str = s[i]

             j = i+1
             while(j<length):
                 if(str+s[j]=='()' or str+s[j]=='[]' or str+s[j]=='{}'):
                     s[i] = '1'
                     s[j] = '1'
                     count+=2
                 print(j)
                 j= j+2
             break;

         if(count==length):
        
            return True
         elif(count<length):

            return False




obj = Solution()

s = '()'
s = '{[]}'
s = '([)]'
s = "[(({})}]"
obj.isValid(s)
