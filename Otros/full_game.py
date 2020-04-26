import triqui

print("\n\tWelcome to the Tic Toc Toe!")
while True:
    the_board = [' ']*9
    player_1_marker, player_2_marker  = triqui.player_input()
    turn = triqui.choose_first()
    play_game = input('\n\tReady to play? y or n:')
    if play_game.lower() == 'y':
        game_on = True
    elif play_game.lower() == 'n':
        game_on = False
        
    while game_on:
        if turn == 'player 1':
            triqui.display_board(the_board)
            position = triqui.player_choice(the_board)
            triqui.place_marker(the_board, player_1_marker, position)
            
            if triqui.win_check(the_board,player_1_marker):
                triqui.display_board(the_board)
                print("\n\tPlayer one has won")
                game_on = False
            else:
                if triqui.full_board_check(the_board):
                    triqui.display_board(the_board)
                    print("\n\tTie game")
                    break
                else:
                    turn = 'player 2'
        else:
            triqui.display_board(the_board)
            position = triqui.player_choice(the_board)
            triqui.place_marker(the_board, player_2_marker, position)
            if triqui.win_check(the_board,player_2_marker):
                triqui.display_board(the_board)
                print("\n\tThe player two has won")
                game_on = False
            else:
                if triqui.full_board_check(the_board):
                    triqui.display_board(the_board)
                    print("\n\tTie game")
                    break
                else:
                    turn = 'player 1'
    if not triqui.replay():
        break
    
    
