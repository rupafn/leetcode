A = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]


def swap(a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

def partition(l,h):
    pivot = A[h]
    i = l-1
    j = h
    
    for j in range(l,h):
        if(A[j] < pivot):
            i = i+1
            swap(i,j)
    swap(i+1,h)
    return (i+1)

def quicksort(l,h):
    if(l<h):
        piv = partition(l,h)
        quicksort(l,piv-1)
        quicksort(piv+1,h)
    


quicksort(0,len(A)-1)
print(A)