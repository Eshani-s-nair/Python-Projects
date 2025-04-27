import random
#create a board 
board=["-","-","-",
       "-","-","-",
       "-","-","-",]
winner=None
current_player="X"
gamerunning=True
def print_board(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("------")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("------")
    print(board[6]+"|"+board[7]+"|"+board[8])

#take player input 
def player_input(board):
    inp=int(input("select a number from 1-9 :  "))
    if 1<=inp<=9 and board[inp-1]=="-":
        board[inp-1]=current_player 
    else:
        print("Oops the other player is already in there..........")    
#computer input
def computer(board):
    pos=random.randint(0,8)
    if 0<=pos<=8 and board[pos]=="-":
        board[pos]=current_player
    elif  board[pos]=="-":
        pos=random.randint(0,8)
        board[pos]=current_player
    elif  board[pos]=="-":
        pos=random.randint(0,8)
        board[pos]=current_player    


#check  win or tie 
def check_horizont(board):
    global winner 
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner =board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner =board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner =board[6]
        return True
    
def check_vert(board):
    global winner 
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner =board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner =board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner =board[2]
        return True
def check_diag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner =board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner =board[2]
        return True
def check_tie(board):
    global gamerunning
    if "-" not in board:
        print_board(board)
        print("It's a tie ...")
        gamerunning=False
        print("-----------GAME OVER--------------")
def check_win():
    global gamerunning
    if check_diag(board) or check_horizont(board) or check_vert(board): 
        gamerunning=False
        print_board(board)
        print(f"the winner is {winner}")
        print("-----------GAME OVER--------------")    
#change player 
def switch_player():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"    
#check win or tie 
while gamerunning==True:
    print_board(board)
    player_input(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)
    switch_player()
    