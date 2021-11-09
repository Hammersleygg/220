"""
Name: Gavin Hammersley
lab10.py

Problem: Create a playable tic-tak-toe game

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def board_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return numbers


def display_board(board):
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("----------")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("----------")
    print("{} | {} | {}".format(board[6], board[7], board[8]))
    print(" ")


def mark_spots(board, position, character):
    # if is_valid(board, position):
    if board[position - 1] != "X" or board[position - 1] != "O":
        board[position - 1] = character


def is_valid(board, position):
    # if there is a x or o in a spot then it is not valid(false) if there isn't a x or o
    # it is valid(true)
    if board[position - 1] == "X" or board[position - 1] == "O":
        return False
    return True


def been_won(board):
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    elif len(board) == 9 and False:
        print("Tie!")

    # cats game
    # i cant seem to get it to print tie yet it is not printing win when it is a tie.


def game_over(board, position):
    if board[position - 1] == " ":
        return False
    return True


def main():
    print("To begin one player should type a position 1-9 followed by a X or O."
          + "\n" "For example 5X. Take turns placing your"
          "X's and O's until someone has won!")
    board = board_numbers()
    display_board(board)
    # mark_spots(board, 5, "X")
    for i in range(1, 10):
        turns = input("please enter where you'd like to place your marker.")
        mark_spots(board, eval(turns[0]), turns[1])
        display_board(board)
        if been_won(board) is True:
            print("Player had won! ")
            break
        if been_won(board) is False:
            print("Tie! ")
            break

    pass


main()
