class Solution:
    def recur(self,wordDict,i,j,mem):

        mem.append(wordDict)

        if(j==len(wordDict)-1):
            j=-1
            i+=1
            return mem[i]
        if(i==len(wordDict)-1 and j==len(wordDict)-1 ):
            return mem
        mem[i] = mem[i]+self.recur(wordDict,i+1,j+1,mem)

    def wordBreak(self, s, wordDict):
        for j in range(0,len(wordDict)):
            str = s
            for k in range(j,len(wordDict)):
                if(wordDict[k] in str):
                    str = str.replace(wordDict[k],'*')
            str = str.replace('*','')
            if(len(str)==0):
                s = str
                break

        if(len(s)==0):
            return True
        return False
        # print(False)

obj = Solution()
s = "applepenapple"
wordDict = ["apple", "pen"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
s ="cars"
wordDict = ["car","ca","rs"]
# s="cbca"
# wordDict = ["bc","ca"]
s = "ccaccc"
word = ["cc","ac"]
print(obj.wordBreak(s,wordDict))
