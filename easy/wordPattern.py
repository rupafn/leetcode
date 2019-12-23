class Solution:
    def wordPattern(self, pattern, str):
        str = str.split(' ')
        pattern = list(pattern)
        dictt = {}
        for p in pattern:
            if p not in dictt:
                dictt[p] = ''
        uniq = list(dictt.keys())
        dictt = {}
        for s in str:
            if s not in dictt:
                dictt[s] = ''
        uniqs = list(dictt.keys())

        dictt = {}
        for i in range(0,len(uniqs)):
            if(i<len(uniq)):
                dictt[uniqs[i]] = uniq[i]
        finallist = []
        for s in str:
            if(s in dictt):
                alp = dictt[s]
                finallist.append(alp)

        if(len(finallist)!=0 and finallist==pattern):
            return True
        return False

        print(pattern)

obj = Solution()


pattern = "abba"
str = "dog cat cat dog"
str = "dog cat cat fish"
pattern = "abba"
str = "dog cat cat fish"
pattern = ''
str = "beef"

print(obj.wordPattern(pattern,str))
