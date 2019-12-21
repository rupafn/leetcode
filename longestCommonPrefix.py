class Solution:
    def longestCommonPrefix(self, strs):
        if(len(strs)==0):
            return ""
        maxPrefCount = 0
        maxPref =''

        for i in range(0,len(strs[0])+1):
            pref = strs[0][0:i]
            flag = True
            for k in strs:
                if(k[0:i] != pref):
                    flag = False
                    break
            if(flag and maxPrefCount<len(pref)):
                maxPrefCount = len(pref)
                maxPref = pref
        return maxPref



obj = Solution()

input = ["flower","flow","flight"]
# input =[]
# input = ["ca","a"]
print(obj.longestCommonPrefix(input))
