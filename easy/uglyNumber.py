class Solution:
    def isPrime(self,n):
        i = 2
        while(i*i<=n):
            # print(n,i,n%i)
            if(n%i==0):
                return False
            i+=1
        return True

    def getPrimeFactors(self,i):
        listt = []
        j = 2
        while(j*j<=i):
            if( i%j==0):
                if(self.isPrime(j)):
                    listt.append(j)
                if(self.isPrime(i//j) and (i//j) not in listt):
                    listt.append(i//j)
            j+=1

        if(self.isPrime(i)):
            listt.append(i)
        return listt


    def isUgly(self, num: int) -> bool:
        if(num<=0):
            return False
        if(num==1):
            return True
        pFactors = [2,3,5]

        primes = self.getPrimeFactors(num)
        print(primes)
        for i in primes:
            if i not in pFactors:
                return False
        return True

        # return True

obj = Solution()

num =6
# num = 214797179
num = 14
num = 937351770
num = 8
print(obj.isUgly(num))
