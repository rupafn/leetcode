class Solution:
    def subtractProductAndSum(self, n):
        n = str(n)
        sum = 0
        prod = 1
        for s in n:
            sum += int(s)
            prod *= int(s)
        return prod-sum



obj = Solution()
n = 234
obj.subtractProductAndSum(n)
