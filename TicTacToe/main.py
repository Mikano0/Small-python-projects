import random

board = [" "] * 9   

def write_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("-------")
    print(board[3], "|", board[4], "|", board[5])
    print("-------")
    print(board[6], "|", board[7], "|", board[8])

def check_win(board, player):
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for combo in wins:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def win_on_next_move(board,player):
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for combo in wins:
        values = [board[i] for i in combo]
        if values.count(player) == 2 and values.count(" ") == 1:
            return combo[values.index(" ")]
    return None

write_board(board)

player = "X"
game_on = True

while game_on:
    if player == "X":
        empty_postions = []
        for position in range(len(board)):
            if board[position]== " ":
                empty_postions.append(position)
        print(empty_postions)

        while True:
            try:
                move = int(input(f"Where do you want to move player {player}? Write a number from 0-8: "))
                if board[move] == " ":
                    board[move] = player
                    break
                else:
                    print("Invalid move. Please choose again")
            except ValueError:
                print("Please enter a valid number")
            except IndexError:
                print("Please enter a number between 0 and 8")

        if check_win(board,player):
            write_board(board)
            print(player, "Wins")
            break
        
        if " " not in board:
            print("Draw")
            break

        write_board(board)

        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        empty_postions = []
        for position in range(len(board)):
            if board[position]== " ":
                empty_postions.append(position)
        print(empty_postions)
        
        
        spot = win_on_next_move(board, player="O")
        if spot is not None:
            board[spot] = player
        else:
            spot = win_on_next_move(board, player="X")
            if spot is not None:
                board[spot] = player
            else:
                if board[4] == " ":
                        board[4] = player
                else:
                    available_corners = []
                    for position in empty_postions:
                        if position in [0,2,6,8]:
                            available_corners.append(position)
                    if available_corners:
                        place = random.choice(available_corners)
                        board[place] = player
                    else:
                        available_sides = []
                        for position in empty_postions:
                            if position in [1,3,5,7]:
                                available_sides.append(position)
                        if available_sides:
                            place = random.choice(available_sides)
                            board[place] = player
        if check_win(board,player):
            write_board(board)
            print(player, "Wins")
            break
        
        if " " not in board:
            print("Draw")
            break

        write_board(board)

        if player == "X":
            player = "O"
        else:
            player = "X"