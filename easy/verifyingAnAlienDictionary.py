class Solution:
    def isAlienSorted(self, words, order):
        dictt = {}
        for i in range(0,len(order)):
            dictt[order[i]]= i
        listCount = [0]*len(words)
        i = 0
        for w in words:
            for j in w:
                listCount[i]+=dictt[j]
            i+=1
        newList = listCount[:]
        listCount.sort()
        if(listCount!=newList):
            return False
        return True


obj = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

# words =  ["word","world","row"]
# order = "worldabcefghijkmnpqstuvxyz"
print(obj.isAlienSorted(words,order))
