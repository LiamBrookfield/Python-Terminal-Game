
from re import sub


class Connectfour:
    row_divider = "+---+---+---+---+---+---+---+"
    col_walls = "|   |   |   |   |   |   |   |"
    x_piece = "| X "
    o_piece = "| O "

    game_lst = [["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"]]


    
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


    def make_play(self, column, piece):
        if piece in "O0oqQ":
            piece = self.o_piece
        else:
            piece = self.x_piece
        if column in range(1, 7) and piece == self.x_piece or piece == self.o_piece:
            print(f"Placing {piece} in column {column}")
            for lst in self.game_lst:
                if lst[column - 1] == "|   ":
                    lst.pop(column - 1)
                    lst.insert((column - 1), piece)
                    return self.game_lst
        print("Invalid piece or column number.")

board1 = Connectfour()
board1.make_play(4, "x")
board1.make_play(4, "0")
board1.make_play(4, "o")
board1.make_play(4, "O")
board1.make_play(4, "P")
board1.make_play(4, "21")
board1.print_current_board()
