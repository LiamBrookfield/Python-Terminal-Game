#Basic Version to conceptualize game


# Idea for gameboard constructor
class GameBoard:
    row_divider = "+---"
    row_divider_end = "+---+"
    col_walls = "|   "
    play_storer = "|   "
        
    def make_board(self, column_num, row_num):
        
        for i in range(row_num):
            print(self.row_divider * (column_num - 1) + self.row_divider_end)
            print(self.col_walls * (column_num + 1))
            print(self.play_storer * (column_num + 1))
            print(self.col_walls * (column_num + 1))
        print(self.row_divider * (column_num - 1) + self.row_divider_end)
    

board1 = GameBoard()
board1.make_board(4, 4)