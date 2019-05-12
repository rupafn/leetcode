arr = [1,2,4,33,7,5,18,2,1]

def sort():
    for i in range(1, len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                print(i)
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
    print(arr)
sort();

# for i in range(19,0,-1):
#     print(i)
