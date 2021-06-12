import minimax, functions
import json

board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
player = 1
player_vs_Ai = int(input("choose the mode( 0 : PvP / 1 : PvAi) "))
mode = int(input("choose the mode( 0 : non stealing / 1 : stealing) "))
if player_vs_Ai == 1:
    difficulty = int(input("choose the difficulty( 0 : easy / 1 : medium / 2 : hard) "))
load = input("to load game press l or p to play new game ")
if load == 'l':
    File_1= open("gamestatus.txt","r")
    game = File_1.readlines() 
    board, player, mode, difficulty, player_vs_Ai = game
    board = json.loads(board)
    player = int(player)
    mode = int(mode)
    difficulty = int(difficulty)
    player_vs_Ai = int(player_vs_Ai)
    File_1.close()
functions.show_game(board)
#input_pos = int(input("choose the position(player 1) "))
case = 'normal'
alpha = float('-inf')
beta = float('inf')
new_turn = 0
while not(functions.game_ended(board[:])):
    
    if player_vs_Ai == 0:
         input_pos = input(f'choose the position(player {player}) OR to save game press s ')
         if input_pos == 's':
             File_1= open("gamestatus.txt","w")
             for l in  [board, player, mode, difficulty, player_vs_Ai]:
                 File_1.writelines(str(l)+"\n")
             File_1.close()
             print("game saved")
             break 
         input_pos = int(input_pos)
         board, player, new_turn= functions.play(board, input_pos, player, mode)
         functions.show_game(board)
         if functions.game_ended(board[:]):
                functions.game_ended(board[:])
                if board[7] > board[0]:
                    print("GG noob player 2")
                elif board[0] > board[7]:
                    print("GG noob player 1")
    else:
        if  player == 1:
            input_pos = input(f'choose the position(player {player}) OR to save game press s ')
            if input_pos == 's':
                File_1= open("gamestatus.txt","w")
                for l in  [board, player, mode, difficulty, player_vs_Ai]:
                    File_1.writelines(str(l)+"\n")
                File_1.close()
                print("game saved")
                break 
            input_pos = int(input_pos)
            board, player, new_turn = functions.play(board, input_pos, player, mode)
            functions.show_game(board)
            if functions.game_ended(board[:]):
                functions.show_game(board)
                if board[7] > board[0]:
                    print("GG noob Ai")
                elif board[0] > board[7]:
                    print("قاتلت بضراوه")
                break
        else:
            if difficulty == 0:
                depth = 2
            elif difficulty == 1:
                depth = 6
            elif difficulty == 2:
                depth = 10
            #print(f"this is board{board}")
            #print(player)
            board_1 = board[:]
            best_move, value = minimax.minimax(board_1, depth, alpha, beta, player, mode,new_turn)
            print(best_move)
            #print(player)
            board, player,new_turn = functions.play(board, best_move, player, mode)
            #print(board)
            functions.show_game(board)
            if functions.game_ended(board[:]):
                functions.game_ended(board[:])
                if board[7] > board[0]:
                    print("GG noob Ai")
                elif board[0] > board[7]:
                    print("قاتلت بضراوه")
                break
        
