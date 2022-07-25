
from re import sub


class Connectfour:
    row_divider = "+---+---+---+---+---+---+---+"
    col_walls = "|   |   |   |   |   |   |   |"
    x_piece = "| X "
    o_piece = "| O "

    game_dict = [["|a  ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|b  ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|c  ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|d  ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|e  ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"],
        ["|f  ", "|   ", "|   ", "|   ", "|   ", "|   ", "|   ", "|"]]


    
    def print_current_board(self):
        dict_string1 = "".join(self.game_dict[0])
        dict_string2 = "".join(self.game_dict[1])
        dict_string3 = "".join(self.game_dict[2])
        dict_string4 = "".join(self.game_dict[3])
        dict_string5 = "".join(self.game_dict[4])
        dict_string6 = "".join(self.game_dict[5])
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


    def make_play(self):
        for lst in self.game_dict:
            print(lst)
          
            
            
            
    

                

                



        
        
board1 = Connectfour()
board1.print_current_board()
board1.make_play()