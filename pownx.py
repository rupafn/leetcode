class Solution:

    def myPow(self, x: float, y: int) -> float:
        if(y == 0):
            return 1
        # print(x,y)
        temp = self.myPow(x, int(y / 2))

        if (y % 2 == 0):
            print('here1',x,y, temp)
            return temp * temp
        else:
            print('here2:',x,y,temp)
            if(y > 0):
                return x * temp * temp
            else:
                return (temp * temp) / x




s = Solution()


s.myPow(4,2)
