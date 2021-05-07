matrix = []
newMatr = []
pathMatrix = []
newPathMatrix = []
for i in range(0,4):
    matrix.append([0]*4)
    newMatr.append([0]*4)
    pathMatrix.append(['']*4)
    newPathMatrix.append(['']*4)

matrix[0][1] = 9
matrix[1][0] = 6
matrix[0][2] = -4
matrix[2][1] = 5
matrix[1][3] = 2
matrix[3][2] = 1

for i in range(0,4):
    for j in range(0,4):
        if(i==j):
            continue
        elif(matrix[i][j]==0):
            matrix[i][j] = 100000

for i in range(0,4):
    for j in range(0,4):
        pathMatrix[i][j] = str(i)+str(j)

for i in range(0,4):
    print(matrix[i])

for i in range(0,4):
    workingCol = i
    workingRow = i
    for j in range(0,4):
        newMatr[workingRow][j] = matrix[workingRow][j]
        newMatr[j][workingCol] = matrix[j][workingCol]
        newPathMatrix[workingRow][j]  = pathMatrix[workingRow][j]
        newPathMatrix[j][workingCol] = pathMatrix[j][workingCol]


    for k in range(0,4):
        for l in range(0,4):
            if(k==l or k==workingRow or l == workingCol):
                continue
            defaultDist = matrix[k][l]
            newDist = matrix[k][i] + matrix[i][l]
            defaultPath = pathMatrix[k][l]
            if(defaultDist<newDist):
                newMatr[k][l] = defaultDist
                newPathMatrix[k][l] = defaultPath

            else:
                newMatr[k][l] = newDist
                newPathMatrix[k][l]= (str(k)+str(i)+str(l))
            # newMatr[k][l] = min(defaultDist,newDist)

    matrix = newMatr
    pathMatrix = newPathMatrix

for i in range(0,4):
    print(pathMatrix[i])

for i in range(0,4):
    print(matrix[i])

# for s in range(0,4):
#     print(matrix[s])
