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
        
    
    def make_board(self):
        self.board = "".join(self.row1_dict.values())
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
print(board1.o_piece)