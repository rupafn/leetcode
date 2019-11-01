matrix =[
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]


def exist(target):
    count = -1;
    for row in matrix:
        count+=1
        length = len(row)
        i = 0;
        j = length-1;

        mid = 0;

        while (i<=j):
            if (j+i)%2==0:
                mid =int((i+j)/2)
            else:
                mid = int(((i+j)-1)/2)
            if(row[mid]==target):
                return True
            if(row[mid]>target):
                j = j-1

            elif(row[mid]<target) :
                i = mid+1
    return False










n = input ("Enter a num: ")

print(exist(int(n)))
