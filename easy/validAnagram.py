class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt = {}
        for i in s:
            if(i in dictt):
                dictt[i]+=1
            else:
                dictt[i] =1
        dictt2={}
        for i in t:
            if(i in dictt2):
                dictt2[i]+=1
            else:
                dictt2[i] =1
        if(dictt!=dictt2):
            return False
        # print(dictt)
        # print(dictt2)

        return True




obj = Solution()

s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
print(obj.isAnagram(s,t))
