
from re import sub


class Connectfour:
    row_divider = "+---+---+---+---+---+---+---+"
    col_walls = "|   |   |   |   |   |   |   |"
    x_piece = "| X "
    o_piece = "| O "

    game_dict = {1: {1: "|a  ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"},
        2: {1: "|b  ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"},
        3: {1: "|c  ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"},
        4: {1: "|d  ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"},
        5: {1: "|e  ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"},
        6: {1: "|f  ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"}}


    
    def print_current_board(self):
        dict_string1 = "".join(self.game_dict.get(1).values())
        dict_string2 = "".join(self.game_dict.get(2).values())
        dict_string3 = "".join(self.game_dict.get(3).values())
        dict_string4 = "".join(self.game_dict.get(4).values())
        dict_string5 = "".join(self.game_dict.get(5).values())
        dict_string6 = "".join(self.game_dict.get(6).values())
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


    def make_play(self, piece):
       for i in self.game_dict:
        for subdict in (self.game_dict.get(i)).values():
            if subdict == "|   ":
                subdict = piece
                print(subdict)
            
            
    

                

                



        
        
board1 = Connectfour()

board1.make_play("| X ")
board1.print_current_board()