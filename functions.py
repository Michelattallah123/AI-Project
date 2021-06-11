def show_game(binAmount):
    print("       13  12  11  10  9   8")
    print("+----+----+----+----+----+----+---+")
    print("|    | " + str(binAmount[13]) + " | " + str(binAmount[12])
          + " | " + str(binAmount[11]) + " | " + str(binAmount[10])
          + " | " + str(binAmount[9]) + " | " + str(binAmount[8]) + " |    |")
    print("|  " + str(binAmount[0]) + " |----+----+----+----+---| " + str(binAmount[7]) + "  |")
    print("|    | " + str(binAmount[1]) + " | " + str(binAmount[2])
          + " | " + str(binAmount[3]) + " | " + str(binAmount[4])
          + " | " + str(binAmount[5]) + " | " + str(binAmount[6]) + " |    |")
    print("+----+----+----+----+----+----+---+")
    print("       1    2  3   4   5  6")


def play(list, input_pos, player, mode):
    new_turn = 0
    copy_list=list[:]
    case = 'normal'
    if mode == 0:
        if player == 1:
            if input_pos in [1, 2, 3, 4, 5, 6]:
                if copy_list[input_pos] != 0:
                    number_stones = copy_list[input_pos]
                    if input_pos + number_stones == 7:
                        case = 'newturn'
                    elif input_pos + number_stones >= 14:
                        case = 'skip'
                    else:
                        case = 'normal'

                    if case == 'normal':
                        for i in range(1, number_stones + 1):
                            copy_list[input_pos + i] = copy_list[input_pos + i] + 1
                        copy_list[input_pos] = 0
                        player = 2
                        #show_game(copy_list)
                    elif case == 'newturn':
                        new_turn = 1
                        for i in range(1, number_stones + 1):
                            copy_list[input_pos + i] = copy_list[input_pos + i] + 1
                        copy_list[input_pos] = 0
                        player = 1
                        #show_game(copy_list)

                    elif case == 'skip':
                        for i in range(1, 13 - input_pos + 1):
                            copy_list[input_pos + i] = copy_list[input_pos + i] + 1
                        for i in range(1, number_stones - (13 - input_pos) + 1):
                            copy_list[i] = copy_list[i] + 1
                        copy_list[input_pos] = 0
                        player = 2
                        #show_game(copy_list)

                else:
                    print("*************************")
                    print("* choose non empty hole *")
                    print("*************************")


            else:
                print("***************")
                print("* wrong entry *")
                print("***************")

        elif player == 2:
            if input_pos in [8, 9, 10, 11, 12, 13]:
                if copy_list[input_pos] != 0:
                    number_stones = copy_list[input_pos]
                    if input_pos + number_stones == 14:
                        case = 'newturn'
                        new_turn = 1
                    elif (input_pos + number_stones) % 14 >= 7 and (input_pos + number_stones) > 14:
                        case = 'skip'
                        new_turn = 0
                    else:
                        case = 'normal'
                        new_turn = 0

                    if case == 'normal':
                        for i in range(1, number_stones + 1):
                            copy_list[(input_pos + i) % 14] = copy_list[(input_pos + i) % 14] + 1
                        copy_list[input_pos] = 0
                        player = 1

                    elif case == 'newturn':
                        new_turn = 1
                        for i in range(1, number_stones + 1):
                            copy_list[(input_pos + i) % 14] = copy_list[(input_pos + i) % 14] + 1
                        copy_list[input_pos] = 0
                        player = 2

                    elif case == 'skip':
                        for i in range(1, 20 - input_pos + 1):
                            copy_list[(input_pos + i) % 14] = copy_list[(input_pos + i) % 14] + 1
                        for i in range(1, number_stones - (20 - input_pos) + 1):
                            copy_list[(i + 7) % 14] = copy_list[(i + 7) % 14] + 1
                        copy_list[input_pos] = 0
                        player = 1

                else:
                    print("*************************")
                    print("* choose non empty hole *")
                    print("*************************")


            else:
                print("***************")
                print("* wrong entry *")
                print("***************")

def all_valid_moves(list, player):
    valid_moves_player_1 = []
    valid_moves_player2 = []
    if player == 2:
        for i in range(8, 14):
            if list[i] != 0:
                valid_moves_player2.append(i)
        return valid_moves_player2
    elif player == 1:
        for i in range(1, 7):
            if list[i] != 0:
                valid_moves_player_1.append(i)
        return valid_moves_player_1


def game_ended(list):
    if (list[1:7] == [0, 0, 0, 0, 0, 0]):
        list[0]+=sum(list[8:14])
        list[8:14] = [0, 0, 0, 0, 0, 0]
        return True
    if (list[8:14] == [0, 0, 0, 0, 0, 0]):
        list[7]+=sum(list[1:7])
        list[1:7] = [0, 0, 0, 0, 0, 0]
        return True
    


# def win(list):
#     winner = 0
    
#     if list[0] > list[7]:
#         winner = 2
#     elif list[7] > list[0]:
#         winner = 1
#     else:
#         winner = 0
#     return winner


def heuristic(list):
    #print(list)
    return list[0] - list[7]
