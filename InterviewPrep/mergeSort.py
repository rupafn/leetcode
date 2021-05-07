
A = [9,3,7,5,6,4,8,2]

def merge(l,mid,h):
    print('left:',A[l:mid])
    print('right:',A[mid:h])
    tmp = []
    for i in range(l,h+1):
        tmp.append(0)
    start= l
    middle= mid
    end = h

    while(start<middle and middle<end):
        if(A[start]<=A[middle])
            tmp[]

    pass


def mergeSort(l,h):
    # print(A[l:h])
    if(l<h):
        mid = (l+h)//2
        mergeSort(l,mid)
        mergeSort(mid+1,h)
        merge(l,mid,h)




mergeSort(0,len(A))
