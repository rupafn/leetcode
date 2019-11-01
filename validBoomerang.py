points = [[0,1],[2,2],[2,0]]
# [[0,1],[1,0],[0,1]]

def isBoomerang() :
    a = points[0]
    b = points[1]
    c = points[2]
    #gradient of ab
    if(a[0]==b[0] and b[0]==c[0]):
        return False;
    if(a[1]==b[1] and b[1]==c[1]):
        return False;
    changey = b[1]-a[1]
    changex = b[0]-a[0]
    grad1 = 11111
    grad2 = 11111

    if(changex!=0):
      grad1 = changey/changex


    newchangey = c[1]-a[1]
    newchangex = c[0]-a[0]
    print(newchangey)
    print(newchangex)
    if(newchangex!=0):
      grad2 = newchangey/newchangex
    # print(grad1)
    # print(grad2)
    if(float(grad1) == float(grad2) or a==b or a==c or b==c):
        return False
    return True;
print(isBoomerang());
