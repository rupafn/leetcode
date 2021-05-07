A = ['A','B','C']
# A = ['1','2','3']
# A= ['B','A','C']
empty_list = []
def swap(s,i,j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp 
    str = ''
    string = str.join(s)
   
    return s
    
def recur(s,left,right,mem):
    
    if left>=right:
        mem.append(''.join(s))
        return 

    for i in range(left,right):
        s = swap(s,i,left)
        recur(s,left+1,right,mem)
        s = swap(s,i,left)
        # s = swap(s,i,left)
    return mem
        
       
        # perm[i] = perm.append(recur(strr,0,len(strr)))
    
        
    

    

    
res = recur(A,0,len(A),[])
# for i in res:
#     print(' '.join(i))
print(res)
print(len(res))


