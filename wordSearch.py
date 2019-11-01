board =[
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]

def exist(str):
    # test = board[0];
    # if 'D' in test:
    #     print('yes')
    for i in range(len(str)):
        col = -1;
        for row in range(len(board)):
            col+=1
            if(str[i] in board[row]):
                if(i!=0):
                    
            # if col in range(len(board[row])):
            #     if(i!=0):
            #         if (count>0)







n = input ("Enter a string: ")

print(exist(n))
