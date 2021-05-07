class Solution:
    def isInterleave(self, s1, s2, s3):
        # if(len(s1)==0 and len(s2)==0 and len(s3)==0):
        #     return 1
        # if(len(s1)==0 and len(s2)==0 and len(s3)!=0):
        #     return 0
        s1 = '0'+s1
        s2 = '0'+s2
        mem = []*len(s2)
        for i in range(0,len(s2)):
            mem.append([0]*len(s1))
        mem[0][0] = 1
        for i in range(1,len(mem[0])):
            print(s3[i-1],s1[i],mem[0][i-1])
            if(s3[i-1]==s1[i] and mem[0][i-1]==1):
                mem[0][i] = 1
        for i in range(1,len(s2)):
            print(s3[i-1],s2[i],mem[i-1][0])
            if(s3[i-1]==s2[i] and mem[i-1][0]==1):
                mem[i][0] = 1
        startRow = 1
        for i in range(1,len(s3)):
            ind = i
            for j in range(1,len(mem[startRow])):
                if(s3[ind]==s1[j]):
                    if(mem[startRow][j-1]==1):
                        mem[startRow][j] = 1
                elif(s3[ind]==s2[startRow]):
                    if(mem[startRow-1][j]==1):
                        mem[startRow][j] = 1

                ind+=1
                if(ind>= len(s3)):
                    break;
            startRow+=1
            if(startRow>= len(s2)):
                break;
        # print(mem)
        return mem.pop()[-1]
        # print(mem[len(s1)-1][len(s2)-1])




obj = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
# s1 = ''
# s2 = ''
# s3 = ''
# s1 = "a"
# s2 = ""
# s3 = "a"
#
# s1 = ""
# s2 = ""
# s3 = "a"
s1 = ""
s2 = "b"
s3 = "b"
print(obj.isInterleave(s1,s2,s3))
