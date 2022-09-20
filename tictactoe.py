# W2 Assignment: Tic-Tac-Toe Game
# Author: Willian Mayer

def main():

    #Starting the game
    print("Welcome to this tic-tac-toe game! ")
    print()
    
    replay = True
    while replay == True:
        player = next_player("")
        board = create_board()
        while not (x_winner(board) or o_winner(board) or is_a_draw(board)):
            display_board(board)
            make_move(player, board)
            player = next_player(player)
        
        display_board(board)
        winner = last_player(player)

        print(f"{winner}'s has won! Good game.")

        replay = input("Do you want to play again (Yes/No)? ")

        if replay == "Yes":
            print()
            replay = True
        elif replay == "No":
            print()
            print("Thanks for playing! See you next time.")
            replay = False

    

def create_board():
    
    board = [" "," "," "," "," "," "," "," "," "]

    return board

def display_board(board):
        print(f"   1 2 3")
        print()
        print(f"1  {board[0]}|{board[1]}|{board[2]}")
        print('   -+-+-')
        print(f"2  {board[3]}|{board[4]}|{board[5]}")
        print('   -+-+-')
        print(f"3  {board[6]}|{board[7]}|{board[8]}")
        print()



    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def x_winner(board):

    return (board[0] == "x" and board[1] == "x" and board[2] == "x" or
            board[3] == "x" and board[4] == "x" and board[5] == "x" or
            board[6] == "x" and board[7] == "x" and board[8] == "x" or
            board[0] == "x" and board[3] == "x" and board[6] == "x" or
            board[1] == "x" and board[4] == "x" and board[7] == "x" or
            board[2] == "x" and board[5] == "x" and board[8] == "x" or
            board[0] == "x" and board[4] == "x" and board[8] == "x" or
            board[2] == "x" and board[4] == "x" and board[6]== "x")

def o_winner(board):

    return (board[0] == "o" and board[1] == "o" and board[2] == "o" or
            board[3] == "o" and board[4] == "o" and board[5] == "o" or
            board[6] == "o" and board[7] == "o" and board[8] == "o" or
            board[0] == "o" and board[3] == "o" and board[6] == "o" or
            board[1] == "o" and board[4] == "o" and board[7] == "o" or
            board[2] == "o" and board[5] == "o" and board[8] == "o" or
            board[0] == "o" and board[4] == "o" and board[8] == "o" or
            board[2] == "o" and board[4] == "o" and board[6]== "o")


def make_move(player, board):
    print(f"{player}'s turn, ")

    square = int(input("Enter a row and column (e.g.: 11) to choose a square: "))
    if square == 11:
        board[0] = player
    elif square == 21:
        board[3] = player
    elif square == 31:
        board[6] = player
    elif square == 12:
        board[1] = player
    elif square == 22:
        board[4] = player
    elif square == 32:
        board[7] = player
    elif square == 13:
        board[2] = player
    elif square == 23:
        board[5] = player
    elif square == 33:
        board[8] = player

    print()


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def last_player(winner):

    if winner == "x":
        return "o"
    elif winner == "o":
        return "x"


main()