class Solution:
    def lastStoneWeight(self, stones):
        while(1):
            if(len(stones)<=1 ):
                break
            y = max(stones)

            indexOfY = stones.index(y)
            stones[indexOfY] = -1
            x = max(stones)
            indexOfX = stones.index(x)
            if(x==y):
                stones.pop(indexOfX)
                stones.pop(indexOfY)
            else:
                stones[indexOfY] =y-x
                stones.pop(indexOfX)
        if(len(stones)==0):
            return 0
        return stones[0]

obj = Solution()
stones = [2,7,4,1,8,1]
stones = [2,2]
print(obj.lastStoneWeight(stones))
