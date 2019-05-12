
dict = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
def getRomanReference(val):
    return dict[val];


def romanToInt(self, s: str) -> int:
    arr = list(s);
    ans = 0;
    num = [];
    for key, val in enumerate(arr):
        num.append(getRomanReference(val))
    # print(len(num))
    for i in range(len(num)):
        if(i+1<len(num) and num[i+1]>num[i]):
            num[i]= -1*num[i]
        ans+=num[i]
    return ans

romanToInt('test','MCMXCIV')
