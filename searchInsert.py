
nums = [1]

def searchInsert(target: int):
    length = len(nums);
    i = 0;
    j = length-1;
    mid = 0;
    while(i<=j):

        if(i+j)%2==0:
            mid = int((i+j)/2)
        else:
            mid = int((i+j-1)/2)

        if(nums[mid]==target):
            return mid
        if(nums[mid]>target):
            j = j-1;
        elif(nums[mid]<target):
            i = mid+1;
    if(mid == length-1 and nums[mid]<target):
        return mid+1
    elif(mid == length-1 and nums[mid]>target):
        return mid
    elif(mid == length-1):
        return mid+1

    return mid;





n = input ("Enter a number: ")

print(searchInsert(int(n)))
