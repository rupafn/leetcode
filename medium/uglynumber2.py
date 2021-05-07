class Solution:
    def genNextPrime(self,flag,prime):
        next = prime+1
        while(next<len(flag)):
            if(flag[next]==0):
                next+=1
            else:
                break
        return next
    def generatePrimes(self,n):
        flag = [1]*(n)
        flag[0] = 0
        prime = 2
        while(prime<(n*2)**(1/2)):
            i = prime*prime
            while(i<len(flag)):
                flag[i] = 0
                i+=prime
            prime = self.genNextPrime(flag,prime)

        return flag

    def getPrimeFactors(self,num):
        listt = []
        while(num%2 ==0):
            num = num/2
            if(2 not in listt):
                listt.append(2)

        for i in range(3,int(n**(1/2))+5,2):
            if(num%i == 0 and i not in [2,3,5]):
                return True
            while(num%i==0):
                num = num/i

        if(num>2):

            return True
            # if(num not in listt):
            #     listt.append(num)

        return False

    def nthUglyNumber(self, n):

        if(n in range(0,7)):
            return n

        i = 6
        x = 7
        num = 1
        valid = [2,3,5]

        listt = [1,2,3,4,5,6]



        while(i<=n):
            hasOtherPrimeFactors = self.getPrimeFactors(x)
            print(x,hasOtherPrimeFactors)
            if(not hasOtherPrimeFactors):
                listt.append(x)
                i+=1
            # print(x,primeFactors)
            # isugly = True
            # for f in primeFactors:
            #     if(f not in valid):
            #         isugly = False
            # if(isugly):
            #     listt.append(x)
            #     i+=1

            x+=1
        print(listt)
        return listt[n-1]


obj = Solution()
n =1650
# n=1
# n = 9
#
# n=7
# n = 23
# n =28
# n = 35
# n = 112
print(obj.nthUglyNumber(n))
