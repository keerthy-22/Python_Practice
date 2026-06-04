def print_board_state(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):  
            print(f" {board[row][col]} ",end="")
            print("|",end="")
        if row != len(board) -1 : # check if it is not last row 
            print("\n------------")
    print()

def is_winner(board,symbol):
    # row lo same symbol 
    for row in range(len(board)): 
        if board[row][0] == board[row][1] == board[row][2] == symbol:
            return True 
    # col lo same symbol 
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True 
    
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True 
        
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True 
    
    return False 

board = [["","",""],
         ["","",""],
         ["","",""]]
players = []
player1 = input("Enter the player-1 name: ")
player2 = input("Enter the player-2 name: ")
players.append(player1)
players.append(player2)
symbols = [player1[0].upper(), player2[0].upper()]
turn = 0 
while True:
    print_board_state(board)
    current_player = players[turn]
    print(f"It's {current_player} Turn: ")
    row = int(input("Enter the row number: "))
    col = int(input("Enter the col number: "))
    board[row-1][col-1] = symbols[turn]
    if is_winner(board,symbols[turn]):
        print_board_state(board)
        print(f"{current_player} is winner")
        break 
    if turn == 0:
        turn = 1
    else: 
        turn = 0 
