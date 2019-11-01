# u,v,w
# starts from city u and arrives at v with a price w.
import math
import time

def getNextLowest(table,visited):
    min = 10000000
    i = 0
    for row in table:
        if(row['mincostfromsrc']<min and row['vertex'] not in visited):
            min = row['mincostfromsrc']
            i = row['vertex']
    return [i,min]

def findCheapestPrice(self, n, flights, src, dst, K):
    #initialization
    node =[[-1 for i in range(n)] for j in range(n)]
    for row in flights:
        node[row[0]][row[1]] = row[2]
    for row in node:
        print(row)
    table = [{
        'vertex':i,
        'mincostfromsrc':1000000000,
        'prevs':''
    } for i in range(n)]
    shortest = math.inf
    table[src]['vertex']= src
    table[src]['mincostfromsrc'] = 0
    visited = [src]
    unvisited = [ i for i in range(n)]

    #End initialization
    cost = table[src]['mincostfromsrc'];
    min = 1000000
    count = 0
    newsrc = src
    t0 = time.time()
    while(1):
        for i in range((len(node[src]))):
            if(node[src][i]!=-1):
                if(table[i]['mincostfromsrc']> cost+node[src][i] and i not in visited):
                    table[i]['mincostfromsrc'] = cost+node[src][i]
                    table[i]['prevs'] = i
                    print('i',i)

        unvisited[src]=-1
        src,cost = getNextLowest(table,visited)
        if(src not in visited):
            visited.append(src)
            print(visited)
            if(src == dst):
                break
        # break;
        if(src in visited):
            break;


    print('cost:',cost)

n = 5
flights =[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst =1
k = 1

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1
#
# n = 3
# flights =[[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0
#
# n = 10
# flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
# src = 6
# dst = 0
# k = 7

print(findCheapestPrice('r',n,flights,src,dst,k))
