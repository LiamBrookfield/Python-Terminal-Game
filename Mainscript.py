
from re import sub


class Connectfour:
    row_divider = "+---+---+---+---+---+---+---+"
    col_walls = "|   |   |   |   |   |   |   |"
    x_piece = "| X "
    o_piece = "| O "

    x_win_condition = False
    o_win_condition = False 

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
        if piece in "O0oqQ.":
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
    
    def check_win_condition(self):
        
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
            

       
           


board1 = Connectfour()
board1.make_move(1, "o")
board1.make_move(1, "o")
board1.make_move(2, "o")
board1.make_move(3, "o")
board1.make_move(4, "x")
board1.make_move(5, "x")
board1.make_move(6, "o")
board1.make_move(7, "x")
board1.make_move(3, "o")
board1.make_move(1, "o")
board1.make_move(1, "o")



board1.print_current_board()
board1.check_win_condition()
print(board1.x_win_condition)
print(board1.o_win_condition)