def myAtoi(self, str: str) -> int:
    str = str.split();
    if(len(str)==0):
        return 0;
    word = str[0];
    ans ='';
    neg = False;
    i=0;
    if(len(word)==1 and (word=='-' or word=='+')):
        return 0;
    for char in word:
        if(i==0 and char=='-'):
            neg = True;
        elif(i==0 and char=='+'):
            neg = False;
        elif (char.isdigit()):
            ans+=char
        else:
            break;
        i+=1;
    if(len(ans)==0):
        return 0;
    ans = int(ans);
    if(neg):
        ans*=-1;
    if(ans>2147483647):
        ans = 2147483647
    elif(ans<-2147483648):
        ans = -2147483648
    return ans;
    print(ans)

myAtoi('ser','3.14159');
