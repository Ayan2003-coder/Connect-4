board=[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]
#1=human 2=AI
#human-minimizer
#AI-maximizer
depth_lim=3
def win():
    for i in range(6):
        for j in range(7):
            if(j<=3):
                if(board[i][j]==1 and board[i][j+1]==1 and board[i][j+2]==1 and board[i][j+3]==1):
                    return 1
                if(board[i][j]==2 and board[i][j+1]==2 and board[i][j+2]==2 and board[i][j+3]==2):
                    return -1
            if(i<=2):
                if(board[i][j]==1 and board[i+1][j]==1 and board[i+2][j]==1 and board[i+3][j]==1):
                    return 1
                if(board[i][j]==2 and board[i+1][j]==2 and board[i+2][j]==2 and board[i+3][j]==2):
                    return -1
            if(i<=2 and j<=3):
                if(board[i][j]==1 and board[i+1][j+1]==1 and board[i+2][j+2]==1 and board[i+3][j+3]==1):
                    return 1
                if(board[i][j]==2 and board[i+1][j+1]==2 and board[i+2][j+2]==2 and board[i+3][j+3]==2):
                    return -1
            if(i>=3 and j>=3):
                if(board[i][j]==1 and board[i-1][j-1]==1 and board[i-2][j-2]==1 and board[i-3][j-3]==1):
                    return 1
                if(board[i][j]==2 and board[i-1][j-1]==2 and board[i-2][j-2]==2 and board[i-3][j-3]==2):
                    return -1
            if(i<=2 and j>=3):
                if(board[i][j]==1 and board[i+1][j-1]==1 and board[i+2][j-2]==1 and board[i+3][j-3]==1):
                    return 1
                if(board[i][j]==2 and board[i+1][j-1]==2 and board[i+2][j-2]==2 and board[i+3][j-3]==2):
                    return -1
            if(i>=3 and j<=3):
                if(board[i][j]==1 and board[i-1][j+1]==1 and board[i-2][j+2]==1 and board[i-3][j+3]==1):
                    return 1
                if(board[i][j]==2 and board[i-1][j+1]==2 and board[i-2][j+2]==2 and board[i-3][j+3]==2):
                    return -1
    return 0


def heuristic(next_player):
    #3 consecutive open(zugzwang) - 900 pts
    #3 consecutive open - 100
    #2 consecutive - 50 pts
    #Every center column piece - 5 pts
    score=0
    factor=None
    if(next_player==1):
        factor=[1,1,0.5]
    else:
        factor=[1,0.5,1]
    for i in range(6):
        for j in range(7):
            #col_zugzwang
            if(board[i][j]==0 and i<=2):
                if(board[i+1][j]!=0 and board[i+1][j]==board[i+2][j]):
                    score+=((-1)**board[i+1][j])*50*factor[board[i+1][j]] #two in a column open
                    if(board[i+2][j]==board[i+3][j]):
                        score+=((-1)**board[i+1][j])*900*factor[board[i+1][j]]

            #row_zugzwang(backwards)
            if(board[i][j]==0 and j>=3):
                if(board[i][j-1]!=0 and board[i][j-1]==board[i][j-2]):
                    score+=((-1)**board[i][j-1])*50*factor[board[i][j-1]] #two in a column open
                    if(board[i][j-2]==board[i][j-3]):
                        if(i==5 or board[i+1][j]!=0):
                            score+=((-1)**board[i][j-1])*900*factor[board[i][j-1]]#zugzwang
                        else:
                            score+=((-1)**board[i][j-1])*100*factor[board[i][j-1]]#3 open
            
            #row_zugzwang(forwards)
            if(board[i][j]==0 and j<=3):
                if(board[i][j+1]!=0 and board[i][j+1]==board[i][j+2]):
                    score+=((-1)**board[i][j+1])*50*factor[board[i][j+1]] #two in a column open
                    if(board[i][j+2]==board[i][j+3]):
                        if(i==5 or board[i+1][j]!=0):
                            score+=((-1)**board[i][j+1])*900*factor[board[i][j+1]]#zugzwang
                        else:
                            score+=((-1)**board[i][j+1])*100*factor[board[i][j+1]]#3 open
                           
                           
                           
            
            #north west zugzwang
            if(board[i][j]==0 and i>=3 and j>=3 and (i==5 or board[i+1][j]!=0)):
                if(board[i-1][j-1]!=0 and board[i-1][j-1]==board[i-2][j-2]):
                    score+=((-1)**board[i-1][j-1])*50*factor[board[i-1][j-1]]
                    if(board[i-2][j-2]==board[i-3][j-3]):
                        score+=((-1)**board[i-1][j-1])*900*factor[board[i-1][j-1]]

            #north east zugzwang
            if(board[i][j]==0 and i>=3 and j<=3 and (i==5 or board[i+1][j]!=0)):
                if(board[i-1][j+1]!=0 and board[i-1][j+1]==board[i-2][j+2]):
                    score+=((-1)**board[i-1][j+1])*50*factor[board[i-1][j+1]]
                    if(board[i-2][j+2]==board[i-3][j+3]):
                        score+=((-1)**board[i-1][j+1])*900*factor[board[i-1][j+1]]

            #south west zugzwang
            if(board[i][j]==0 and i<=2 and j>=3 and (i==5 or board[i+1][j]!=0)):
                if(board[i+1][j-1]!=0 and board[i+1][j-1]==board[i+2][j-2]):
                    score+=((-1)**board[i+1][j-1])*50*factor[board[i+1][j-1]]
                    if(board[i+2][j-2]==board[i+3][j-3]):
                        score+=((-1)**board[i+1][j-1])*900*factor[board[i+1][j-1]]

            #south east zugzwang
            if(board[i][j]==0 and i<=2 and j<=3 and (i==5 or board[i+1][j]!=0)):
                if(board[i+1][j+1]!=0 and board[i+1][j+1]==board[i+2][j+2]):
                    score+=((-1)**board[i+1][j+1])*50*factor[board[i+1][j+1]]
                    if(board[i+2][j+2]==board[i+3][j+3]):
                        score+=((-1)**board[i+1][j+1])*900*factor[board[i+1][j+1]]

            if(board[i][j]!=0 and j==3):
                score+=((-1)**board[i][j])*5 #center piece


            left,right=[i,j],[i,j]
    return score


            
            
            

def full():
    for a in board:
        if(0 in a):
            return False
    return True         
                


def minmax(player,depth,alpha,beta): #return score of a board configuration
    res=win()
    if(res==1):
        return -10000
    elif(res==-1):
        return 10000
    else:
        if(full()):
            return 0
        if(depth>=depth_lim):
            if(player==1):
                return heuristic(2)
            return heuristic(1)
        score=None
        if(player==1):
            score=10**9+7
        else:
            score=-10**9+7
        for i in range(7):
            if(alpha>=beta):
                break
            for j in range(5,-1,-1):
                if(board[j][i]==0):
                    board[j][i]=player
                    if(player==1):
                        sc=minmax(2,depth+1,alpha,beta)
                        score=min(score,sc)
                        beta=min(beta,sc)
                    else:
                        sc=minmax(1,depth+1,alpha,beta)
                        score=max(score,sc)
                        alpha=max(alpha,sc)
                    board[j][i]=0
                    break
        return score
        

            

def show():
    blank = "\u26AB"  #black circle
    ai = "\U0001F534"  #red circle
    human = "\U0001F7E1"  #yellow circle
    print("Blank:",blank," Human:",human, " AI:",ai)
    symbols=[blank,human,ai]
    for i in range(6):
        print("|",end="")
        for j in range(7):
              print(" ",symbols[board[i][j]],end=" ")
        print("|\n")
            
    


player=2
while(True):
    res=win()
    if(res==1):
        print("Human wins")
        break
    elif(res==-1):
        show()
        print("AI wins")
        break
    else:
        if(full()):
            print("Draw")
            break
        if(player==1):
            show()
            mov=None
            while(True):
                mov=int(input("Enter move : "))
                if(mov<1 or mov>7 or board[0][mov-1]!=0):
                    print("Invalid move, try again")
                else:
                    break
            for i in range(5,-1,-1):
                if(board[i][mov-1]==0):
                    board[i][mov-1]=1
                    break
            player=2
        else:
            move=None
            score=-10**9+7
            for col in range(7):
                row=None
                for r in range(5,-1,-1):
                    if(board[r][col]==0):
                        row=r
                        break
                if(row!=None):
                    board[row][col]=2
                    sc=minmax(1,0,-10**9+7,10**9+7)
                    if(sc>=score):
                        score=sc
                        move=(row,col)
                    board[row][col]=0
            board[move[0]][move[1]]=2
            player=1
                    
            
                
        
        

