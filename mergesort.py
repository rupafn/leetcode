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
    print(result)

def swap(left,right):
    tmp = a[left]
    a[left] = a[right]
    a[right] = tmp
    return left

# mergesort();
def partition(i,j,pivot):
    left = i
    right = j
    needTochange1 = False
    needTochange2 = False
    while(left<right):
        if(a[left] > a[pivot]):
            needTochange1 = True
            pass
        else:
            left += 1
        if(a[right] < a[pivot]):
            needTochange2 = True
            pass
        else:
            right -= 1
        if(needTochange1 and needTochange2):
            swap(left,right)
            needTochange1 = False
            needTochange2 = False

    return swap(right,pivot)
     # return arr




def quickSort(left, right):
    pivot = left
    if(right-left<0):
        return
    j = partition(left,right,pivot)
    quickSort(0,j-1)
    quickSort(j+1,right)

    # quickSort()

    return 0






a = [10,16,8,12,15,6,3,9,5]
left = 0
right = len(a)-1
quickSort(left,right)
print(a)
