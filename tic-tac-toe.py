'''A command line  tic-tac-toe game'''

#Game board 3rows and 3 columns
board=[[1,2,3],[4,5,6],[7,8,9]]
player1= 'X'
player2= 'O'

#Draws the board to the screen
def draw_board(board):
    for row in board:
        print(*row,sep='|')

#checks if a move is valid or not. returns a bool
def check_valid_move(move,board)-> bool:
    #validates if the  move is a valid location in the board
    if move not in str('123456789'):
        print("invalid move.")
        return False
    #validates if the move location is not occupied in the board
    if move not in str(board):
        print("Invalid move. The spot has been occupied")
        return False
        
    return True
#inserts a player in a location on the board
def insert_player(move,player,board):
    for row in range(len(board)):#iterates over the rows of the board
        for column in range(len(board[row])):#iterates over the boards column
            value=board[row][column] 
            if str(value) == move: #if the location is found
                board[row][column]=player #adds the player
                
#checks if there is a winner. Return a string if there is a winner or none if no winner            
def check_winner(board)->str or None :
    #comnination to get board values based on row, column, diagonal
    combinations = [
    [(0,0),(0,1),(0,2)],#1,2,3
    [(1,0),(1,1),(1,2)],#4,5,6
    [(2,0),(2,1),(2,2)],#7,8,9
    [(0,0),(1,0),(2,0)],#1,4,7
    [(0,1),(1,1),(2,1)],#2,5,8
    [(0,2),(1,2),(2,2)],#3,6,9
    [(0,0),(1,1),(2,2)],#1,5,9
    [(0,2),(1,1),(2,0)]]#3,5,7

    for combination in combinations:#iterates over the combinations
        values=[] #empty list to store the board values based on the combination
        for row,col in combination: # iterates over a row and column of a combination
            values.append(board[row][col])#appends 3 board values to the value list
        if values[0]==values[1]==values[2]:#checks whether all the values in the values list are the same
            return values[0]#returns the winner if the  values match
#returns  the current player's turn based on the previous turn
def whose_turn(previous_turn):
    if previous_turn == player1: #returns player1 if previous turn is none or player2
        return player2
    return player1
#gameplay main screen
def start():
    print("********WELCOME TO TIC-TAC-TOE GAME**********")#displays welcome message
    print("player1:X    player2:O")
    previous_turn=None 
    winner_found= False
    draw_board(board)
    possible_moves=9 #number of possible moves
    print(f"\nplayer1 starts")
    while not winner_found and possible_moves >0:#iterates until a winner is found or possible moves is zero
        move=str(input(f"{whose_turn(previous_turn)}  enter your move:"))
        
        if check_valid_move(move,board):#validates if a move is valid 
            insert_player(move,whose_turn(previous_turn),board)#inserts the move
            possible_moves-=1#subtracts a move from possible moves after inserting it 
            draw_board(board)
            if check_winner(board) is not None: #checks if there is a winner
                print(f'{check_winner(board)}  wins the game' )
                winner_found=True
            if check_winner(board) is None and possible_moves  == 0:#if no winner is found and no of possible moves is 0
                print("The game ends with a draw")
                break
                
            previous_turn=whose_turn(previous_turn)#alternates the players
            
        
start()#starts the game       
    
    
