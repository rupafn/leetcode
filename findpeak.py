arr = [1,2,15,3,6,18,21,2,87,3,14]


def findpeak(n):
    print(n)
    print(arr[n])
    if(n ==len(arr)-1 and arr[n]>= arr[n-1]):
        return n;
    if(n == 0 and arr[n]>= arr[n+1]):
        return n;
    if(arr[n]>=arr[n-1] and arr[n]>=arr[n+1] ):
        return n
    if(arr[n]<arr[n-1]):
        if(n%2!=0):
            findpeak(int((n-1)/2))
        else:
            findpeak(int(n/2));
    if(arr[n]<arr[n+1]):
        length = len(arr)-1
        right = length -n
        midright = int(right/2)
        if(right%2!=0):
          midright = int((right-1)/2)

        return findpeak(n+midright)




n = len(arr)
n= int((n-1)/2)
# print(n)
arr.sort();
t = findpeak(n)
print(arr[t])
