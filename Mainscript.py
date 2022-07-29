
from multiprocessing.sharedctypes import Value
from re import sub
from os import system


class Connectfour:
    row_divider = "+---+---+---+---+---+---+---+"
    col_walls = "|   |   |   |   |   |   |   |"
    x_piece = "| X "
    o_piece = "| O "

    x_win_condition = False
    o_win_condition = False 
    tie_condition = False

    game_lst = [["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"]]


    # Takes the nested lists of game_lst and formats them into a long multi-line string. When called prints the
    # connect 4 board in its current state.

    def print_current_board(self):
        dict_string1 = "".join(self.game_lst[0])
        dict_string2 = "".join(self.game_lst[1])
        dict_string3 = "".join(self.game_lst[2])
        dict_string4 = "".join(self.game_lst[3])
        dict_string5 = "".join(self.game_lst[4])
        dict_string6 = "".join(self.game_lst[5])
        self.board = (f"""  1   2   3   4   5   6   7
{self.row_divider}
{self.col_walls}
{dict_string6}
{self.col_walls}
{self.row_divider}
{self.col_walls}
{dict_string5}
{self.col_walls}
{self.row_divider}
{self.col_walls}
{dict_string4}
{self.col_walls}
{self.row_divider}
{self.col_walls}
{dict_string3}
{self.col_walls}
{self.row_divider}
{self.col_walls}
{dict_string2}
{self.col_walls}
{self.row_divider}
{self.col_walls}
{dict_string1}
{self.col_walls}
{self.row_divider}""")
    
        print(self.board)



    # Logic for adding a piece to the game board. Alters the nested lists inside of game_lst above which then changes the output of print_current_board.

    def make_move(self, column, piece):
        if piece in "O0oqQ.*p38?@ooooOOOOO":
            piece = self.o_piece
        else:
            piece = self.x_piece
        if column in range(1, 8) and piece == self.x_piece or piece == self.o_piece:
            print(f"Placing {piece} in column {column}")
            for lst in self.game_lst:
                if lst[column - 1] == "|   ":
                    lst.pop(column - 1)
                    lst.insert((column - 1), piece)
                    return self.game_lst
        print("Invalid piece or column number.")

    
    # Iterates through game_lst and tries to find four connected pieces
    
    def check_win_condition_horizontal(self):
        
        # Horizontal Check
    
        for lst in self.game_lst:
            if ((lst[0:4].count(self.x_piece)) >= 4 or 
            (lst[1:5].count(self.x_piece)) >=4 or 
            (lst[2:6].count(self.x_piece)) >=4 or 
            (lst[3:7].count(self.x_piece)) >=4):
                self.x_win_condition = True
                return self.x_win_condition
        for lst in self.game_lst:
            if ((lst[0:4].count(self.o_piece)) >= 4 or 
            (lst[1:5].count(self.o_piece)) >=4 or 
            (lst[2:6].count(self.o_piece)) >=4 or 
            (lst[3:7].count(self.o_piece)) >=4):
                self.o_win_condition = True
                return self.o_win_condition


    def check_win_condition_vertical(self):

        # Vertical Check
        
        for tupl in zip(self.game_lst[0], self.game_lst[1], self.game_lst[2], self.game_lst[3], self.game_lst[4], self.game_lst[5]):
            if ((tupl[0:4].count(self.x_piece)) >= 4 or 
            (tupl[1:5].count(self.x_piece)) >=4 or 
            (tupl[2:6].count(self.x_piece)) >=4):
                self.x_win_condition = True
                return self.x_win_condition
            if ((tupl[0:4].count(self.o_piece)) >= 4 or 
            (tupl[1:5].count(self.o_piece)) >=4 or 
            (tupl[2:6].count(self.o_piece)) >=4):
                self.o_win_condition = True
                return self.o_win_condition

    def check_win_condition_diagonal(self):

        # Diagonal Check /
        x = 0
        y = 0
        for lst in self.game_lst:
            x = 0
            for piece in lst:
                if (self.game_lst[y][x] == self.x_piece and
                self.game_lst[y+1][x+1] == self.x_piece and
                self.game_lst[y+2][x+2] == self.x_piece and
                self.game_lst[y+3][x+3] == self.x_piece):
                    self.x_win_condition = True
                    return self.x_win_condition 
                x += 1
                if x > 3:
                    break
            y += 1
            if y > 2:
                break
        x = 0
        y = 0
        for lst in self.game_lst:
            x = 0
            for piece in lst:
                if (self.game_lst[y][x] == self.o_piece and
                self.game_lst[y+1][x+1] == self.o_piece and
                self.game_lst[y+2][x+2] == self.o_piece and
                self.game_lst[y+3][x+3] == self.o_piece):
                    self.o_win_condition = True
                    return self.o_win_condition 
                x += 1
                if x > 3:
                    break
            y += 1
            if y > 2:
                break

            # Diagonal Check \

        x = 0
        y = 0
        for lst in self.game_lst:
            x = -2
            for piece in lst:
                if (self.game_lst[y][x] == self.x_piece and
                self.game_lst[y+1][x-1] == self.x_piece and
                self.game_lst[y+2][x-2] == self.x_piece and
                self.game_lst[y+3][x-3] == self.x_piece):
                    self.x_win_condition = True
                    return self.x_win_condition 
                x -= 1
                if x < -5:
                    break
            y += 1
            if y > 2:
                break
        x = 0
        y = 0
        for lst in self.game_lst:
            x = -2
            for piece in lst:
                if (self.game_lst[y][x] == self.o_piece and
                self.game_lst[y+1][x-1] == self.o_piece and
                self.game_lst[y+2][x-2] == self.o_piece and
                self.game_lst[y+3][x-3] == self.o_piece):
                    self.o_win_condition = True
                    return self.o_win_condition 
                x -= 1
                if x < -5:
                    break
            y += 1
            if y > 2:
                break

    # Tie check looks through the game list and tries to find "|   ". If not present then a sets tie condition to true.

    def check_tie_condition(self):
        if not any("|   " in sl for sl in self.game_lst):
            self.tie_condition = True
            return self.tie_condition
    


game = Connectfour()

def tutorial():
    system("clear")
    print("Welcome to Connect Four! To get started enter the column number you wish to place a piece into (a number from 1 to 7).")

    game.print_current_board()

    first_column = int(input())
    print(f"Column number {first_column} selected.")
    print("Great! Now pick a piece to enter into that column. You can choose between X and O - if what you type is roughly O shaped it'll be an O. Otherwise you'll get an X, so be careful player O.")
    first_piece = str(input())

    system("clear")

    game.make_move(first_column, first_piece)

    print("You got it - now the game is on. Be the first to connect four pieces to win. Good luck!")
    return game

answer = (str(input("Skip Tutorial? (Y/N): "))).lower()
if answer == "n":
    tutorial = tutorial()

def play_game(game = game):
    while game.x_win_condition == False and game.o_win_condition == False and game.tie_condition == False:
        system("clear")
        game.print_current_board()
        try: 
            game.make_move(int(input("Enter Column Number: ")), str(input("Enter piece (X or O): ")))
        except ValueError:
            print("Invalid piece or column number.")
        game.check_win_condition_horizontal()
        game.check_win_condition_vertical()
        game.check_win_condition_diagonal()
        game.check_tie_condition()
    
    if game.x_win_condition == True:
        system("clear")
        game.print_current_board()
        print("X is the winner! This script will now end. Ciao :)")
    elif game.o_win_condition == True:
        system("clear")
        game.print_current_board()
        print("O is the winner! This script will now end. Ciao :)")
    elif game.tie_condition == True:
        system("clear")
        game.print_current_board()
        print("Looks like nobody wins :(")

play_game = play_game()