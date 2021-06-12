import functions

def minimax(list, depth, alpha, beta, player, mode):
    value = 0
    best_move = 0
    if depth == 0:
        return -10, functions.heuristic(list)
    if player == 2:
        print(f"this is list{list}")
        value = float('-inf')
        valid_moves = functions.all_valid_moves(list, player)
        print(valid_moves)
        for i in valid_moves:
            board_now, player = functions.play(list, i, player, mode)
            print(player)
            #functions.show_game(board_now)
            x, y = minimax(board_now, depth-1, alpha, beta, 1, mode)
            if value != max(value, y):
                best_move = i
            value = max(value, y)
            alpha = max(alpha, value)
            # if alpha >= beta:
            #     break
        return best_move, value
    elif player == 1:
        #print("i am here")
        value = float('inf')
        valid_moves = functions.all_valid_moves(list, player)
        print(valid_moves)
        for i in valid_moves:
            board_now, player = functions.play(list, i, player, mode)
            print(player)
            #functions.show_game(board_now)
            value = min(value, minimax(board_now, depth - 1, alpha, beta, 2, mode)[1])
            beta = min(beta, value)
            if beta <= alpha:
                break
        return -10, value


