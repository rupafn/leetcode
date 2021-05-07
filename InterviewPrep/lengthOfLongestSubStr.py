class Solution:
    def lengthOfLongestSubstring(self, s) :

        if(len(s)==1 or len(s)==0):
            return len(s)
        arr = []
        maxlen = 0
        i = 0
        while(i<len(s)-1):
            tmp = []
            flag = True
            for j in range(i,len(s)):
                if(s[j] not in tmp ):
                    tmp.append(s[j])
                else:
                    i = j
                    flag = False
                    break
            if(len(tmp) > maxlen):
                maxlen = len(tmp)

            arr.append(tmp)
            if(flag):
                i+=1
        return maxlen


obj = Solution()
s = "abcabcbb"
s = "bbbbb"
# s = "pwwkew"
# s = 'abcd'
# s='cdd'
# s = 'abcb'
# s = " "
print(obj.lengthOfLongestSubstring(s))
