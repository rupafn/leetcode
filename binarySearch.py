import math
#             i             j
nums = [1,3,4,5,13,20,25,40,42,44,53]


def search(n):
    length = len(nums)
    i = 0;
    j = length-1;

    mid = 0;

    while (i<=j):
        if (j+i)%2==0:
            mid =int((i+j)/2)
        else:
            mid = int(((i+j)-1)/2)
        if(nums[mid]==n):
            return mid;
        if(nums[mid]>n):
            j = j-1

        elif(nums[mid]<n) :
            i = mid+1
    return -1



n = input ("Enter a number: ")

print(search(int(n)))
