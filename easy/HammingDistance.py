class Solution:
    def toBinary(self,num):
        listt = []
        while(num>1):
            listt.append(int(num%2))
            num=num/2
        listt.append(int(num))
        listt.reverse()
        return listt
    def hammingDistance(self, x, y):
        x = self.toBinary(x)
        y = self.toBinary(y)
        if(len(y)>len(x)):

            newl = []
            for i in range(0, len(y)-len(x)):
                newl.append(0)
            x = newl + x

        elif(len(x)>len(y)):
            newl = []
            for i in range(0, len(x)-len(y)):
                newl.append(0)
            y = newl + y
        count = 0
        for i in range(0,len(y)):
            if(x[i]!=y[i]):
                count+=1
        # print(count, x,y)
        return count


        pass


obj = Solution()
x = 1
y = 4

# x = 4
# y = 14
obj.hammingDistance(x,y)
