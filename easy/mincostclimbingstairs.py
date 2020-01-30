class Solution:
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        cost.append(0)
        for j in range(2,length+1):
            # print(cost[j]+min(cost[j-1],cost[j-2]))
            cost[j] =cost[j]+min(cost[j-1],cost[j-2])

        return cost.pop()


obj = Solution()
cost = [10, 15, 20]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(obj.minCostClimbingStairs(cost))
