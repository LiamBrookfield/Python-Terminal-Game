#Basic Version to conceptualize game


# Idea for gameboard constructor
class Connectfour:
    row_divider = "+---+---+---+---+---+---+---+"
    col_walls = "|   |   |   |   |   |   |   |"
    x_piece = ["| X "]
    o_piece = ["| O "]

    row1_dict = {1: "|   ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"}
    row2_dict = {1: "|   ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"}
    row3_dict = {1: "|   ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"}
    row4_dict = {1: "|   ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"}
    row5_dict = {1: "|   ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"}
    row6_dict = {1: "|   ", 2: "|   ", 3: "|   ", 4: "|   ", 5: "|   ", 6: "|   ", 7: "|   ", 8: "|"}
        
    
    def print_current_board(self):
        dict_string1 = "".join(self.row1_dict.values())
        dict_string2 = "".join(self.row2_dict.values())
        dict_string3 = "".join(self.row3_dict.values())
        dict_string4 = "".join(self.row4_dict.values())
        dict_string5 = "".join(self.row5_dict.values())
        dict_string6 = "".join(self.row6_dict.values())
        self.board = (f"  1   2   3   4   5   6   7\n{self.row_divider}\n{self.col_walls}\n{dict_string1}\n{self.col_walls}\n{self.row_divider}\n{self.col_walls}\n{dict_string2}\n{self.col_walls}\n{self.row_divider}\n{self.col_walls}\n{dict_string3}\n{self.col_walls}\n{self.row_divider}\n{self.col_walls}\n{dict_string4}\n{self.col_walls}\n{self.row_divider}\n{self.col_walls}\n{dict_string5}\n{self.col_walls}\n{self.row_divider}\n{self.col_walls}\n{dict_string6}\n{self.col_walls}\n{self.row_divider}")
    
        print(self.board)


    def make_move(self):
        print("  1   2   3   4   5   6   7")
        for i in range(6):
            print(self.row_divider)
            print(self.col_walls)
            print("".join(self.row1_dict.values()))
            print(self.col_walls)
        print(self.row_divider)
        
        
board1 = Connectfour()
board1.make_board()