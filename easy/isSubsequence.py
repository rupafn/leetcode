class Solution:
    def isSubsequence(self, s, t):
        if(len(s)==0):
            return False
        length = len(t)
        k = 0
        for i in range(0,length):
            if(s[k]==t[i]):
                k+=1
            if(k==len(s)):
                break
        # print(k)
        if(k == len(s)):
            return True
        return False


obj = Solution()
s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"
s = ""
t = "ahbgdc"
print(obj.isSubsequence(s,t))
