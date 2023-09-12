PLAYER_X='X'
player_y='y'
empty=' '
#defining the tic tac toe as a 3*3 list
board=[
        [empty,empty,empty],
        [empty,empty,empty],
        [empty,empty,empty]
]
def print_board(board):
    for row in board:
        print('|'.join(row)) #print each of the elements separated by a |
        print("------------") #after each row a dashed line is printed
def is_full(board): #this function will check if the board is full or not
    for row in board:
        if empty in row:
            return False
    return True
def check_winner(board,player):
    for row in board:
        if all(cell==player for cell in row):
            return True #we have checked here in each row
        for col in range(3):#here we will check for each column
            if all(board[row][col]==player for row in range(3)):
                return True
        #for top left to bottom diagonal
        if all(board[i][i]==player for i in range(3)):
            return True
        #now a diagonal from top right to bottom left
        if all(board[i][2-i]==player for i in range(3)):
            return True
def evaluate_winner(board):
    if check_winner(board,PLAYER_X):
        return 10
    elif check_winner(board,player_y):
        return -10
    else:
        return None
##IMPLIMENTATION OF MINIMAX ALGORITHM
def minimax(board,depth,maximizing_player):
    score=evaluate_winner(board)
    if score is not None:
        return score
    if maximizing_player:
        max_eval=float('-inf')
        for row in range(3):
            for column in range(3):
                if board[row][column]==empty:
                    board[row][column]=PLAYER_X
                    eval=minimax(board,depth+1,False)
                    board[row][column]=empty
                    max_eval=max(max_eval,eval)
        return max_eval
    else:
        min_eval=float('inf')
        for row in range(3):
            for column in range(3):
                if board[row][column]==empty:
                    #to check out all the possibilites we will hypothetically move or place player_y
                    #and later again make that place empty
                    board[row][column]=player_y
                    eval=minimax(board,depth+1,True)
                    board[row][column]=empty
                    min_eval=min(min_eval,eval)
        return min_eval
def find_best_move():
    best_move=None
    best_eval=float('-inf')
    for row in range(3):
        for col in range(3):
            if board[row][col]==empty:
                board[row][col]=PLAYER_X
                eval=minimax(board,0,False)
                board[row][col]=empty
                if eval>best_eval:
                    best_eval=eval
                    best_move=(row,col)
    return best_move
#this is the main code 
while True:
    print_board(board)
    player_move=input("enter the move (row and column)")
    row,col=map(int,player_move.split())
    if board[row][col]!=empty:
        print("invalid move")
        continue
    board[row][col]=PLAYER_X
    if check_winner(board,PLAYER_X):
        print_board(board)
        print("you win!!")
        break
    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break

    print("Computer's move:")
    computer_move = find_best_move()
    board[computer_move[0]][computer_move[1]] = player_y

    if check_winner(board, player_y):
        print_board(board)
        print("Computer wins!")
        break

    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break
