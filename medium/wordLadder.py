class Solution:
    def rec(self,beginWord, endWord, wordList,arr):
        if(beginWord == endWord):
            print('ues')

        for j in range(0,len(wordList)):
            print(wordList[j],beginWord)
            diff = list(set(beginWord) - set(wordList[j]))
            # print(beginWord,diff,wordList[j])
            if(wordList[j]!=beginWord and len(diff) ==1):
                arr.append(wordList[j])
                # beginWord = wordList[j]
                if(wordList[j] == endWord):
                    return arr
                return self.rec(wordList[j],endWord,wordList[0:j]+wordList[j+1:],arr)

        return []
    def ladderLength(self, beginWord, endWord, wordList):

        for i in range(0,len(wordList)):
            diff = list(set(beginWord) - set(wordList[i]))
            # print(diff)
            if(wordList[i]!=beginWord and len(diff) ==1):
                arr = [beginWord,wordList[i]]
                arrInd = [i]
                print(self.rec(wordList[i],endWord,wordList[0:i]+wordList[i+1:],arr))


wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"
# #
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# #
# beginWord ="a"
# endWord ="c"
# wordList =["a","b","c"]


# #
# beginWord ="hot"
# endWord ="dog"
# wordList =["hot","dog","dot"]
obj = Solution()
obj.ladderLength(beginWord,endWord,wordList)
