class Solution:
    def dp(self,n,i,mem,count):
        if(i>n):
            count = count+1
            return 0


        if(i==n):
            return 1

        if (mem[i] > 0):
            # print(type(mem[i]))
            return mem[i];

        # print(type(self.dp(n,i+1,mem)))
        return self.dp(n,i+1,mem,count) + self.dp(n,i+2,mem,count)

        return count


    def climbStairs(self, n):
        if(n ==1):
            return 1
        if(n==0):
            return 0
        mem = [0]*n
        mem[0]=1
        mem[1]=2

        for i in range(2,n):
            mem[i] = mem[i-1]+mem[i-2]

        return mem[n-1]



obj = Solution()
obj.climbStairs(1)
