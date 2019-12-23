class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        length = len(bits)
        while(i<length):
            if(bits[i:i+2] == [1,0] or bits[i:i+2] == [1,1]):
                i = i+2
            else:
                if(i==length-1):
                    return True
                i = i+1


            # if(bits[i:i+2])
        return False

obj = Solution()
bits = [1, 0, 0]
bits = [0]
bits = [1, 1, 1, 0]
bits = [1, 0, 0]
print(obj.isOneBitCharacter(bits))
