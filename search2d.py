matrix =[
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
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
                Found = True;
                return True
            if(row[mid]>target):
                j = j-1

            elif(row[mid]<target) :
                i = mid+1
    return False










n = input ("Enter a num: ")

print(exist(int(n)))
