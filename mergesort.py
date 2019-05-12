num1 = [2,4,8,9,15,34]
num2 = [1,2,3,4,5,6,12,13,20,22,23,25]
# num1 = []
#
# num2 = [2,3]
def mergesort():
    a = [];
    b = [];
    result = []
    if(len(num1)<len(num2)):
        a = num1
        b = num2
    else:
        a = num2
        b = num1
    i = 0;
    j = 0;
    while(1):
        if(len(a)==0):
            if(len(b)>0):
                result = result+b
            break;
        if( len(b)==0):
            if(len(a)>0):
                result = result+a
            break;
        if a[i]<b[j]:
            result.append(a.pop(i))
        else:
            result.append(b.pop(i))

    length = len(result);

    median = 0;
    median = result[int((length-1)/2)]
    if length%2==0:
        median = (result[int(length/2)] + result[int(length/2-1)])/2
    print(median)
    return float(median)





mergesort();
