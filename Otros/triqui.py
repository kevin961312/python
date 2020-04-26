import random
def display_board(board):
        print("\n\t   |   |   ")
        print("\t {} | {} | {} ".format(board[0].upper(),board[1].upper(),board[2].upper()))
        print("\t   |   |   ")
        print("\t------------")
        print("\t   |   |   ")
        print("\t {} | {} | {} ".format(board[3].upper(),board[4].upper(),board[5].upper()))
        print("\t   |   |   ")
        print("\t------------")
        print("\t   |   |   ")
        print("\t {} | {} | {} ".format(board[6].upper(),board[7].upper(),board[8].upper()))
        print("\t   |   |   ")

def player_input():
    while True:
        player1 = input("\n\tPlease pick a marker 'X' or 'O':\n\t")
        if player1.lower() == 'x':
            print("\n\tThe player one has "+player1.upper().strip()+".")
            print("\n\tThe player two has O.")
            marker = ('x','o')
            return marker
            break
        elif player1.lower() == 'o':
            print("\n\tThe player one has "+player1.upper().strip()+".")
            print("\n\tThe player two has X.")
            marker = ('o','x')
            return marker
            break
            
def place_marker(board, marker, position):
    board[position] = marker 
        
def win_check(board, mark):
    return ((board[0] == board[1] == board[2] == mark) or
    (board[3] == board[4] == board[5] == mark) or
    (board[6] == board[7] == board[8] == mark) or
    (board[0] == board[3] == board[6] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[0] == board[4] == board[8] == mark) or
    (board[2] == board[4] == board[6] == mark))
 
def choose_first(): 
    number_first = random.randint(1, 2)
    if number_first == 1:
        print("\n\tThe first to play is player one.")
        return 'player 1'
    elif number_first == 2:
        print("\n\tThe first to play is player two.")
        return "player 2"

def space_check(board, position):
    return board[position] == ' '        
       
def full_board_check(board):
    for i in range(0,9):
        if space_check(board, i):
            return False
    return True
    
def player_choice(board):
    position = -1
    while position not in [0,1,2,3,4,5,6,7,8] or not space_check(board, position):
        try:
            position = int(input("\n\tWhat is your next position (1-9)?: "))-1
        except  ValueError:
            print("\n\tYou have to enter a number, thanks you!")        
    return position

def replay():
    return input('\n\tPlay again? enter Y or N: ').startswith('y')    
    

